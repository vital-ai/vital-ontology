"""Check that the owl:imports closure of every domain ontology resolves to a
local OWL file in this repository.

Usage:
    python tools/check_imports.py

Scans vital-ontology/ and domain-ontology/ for .owl files, builds an
IRI -> file map, then walks owl:imports transitively from each ontology and
reports any IRIs that do not resolve to a local file. Also prints the
dependency chain in topological (build) order.

Exit code 0 if the closure is complete, 1 otherwise.
"""

import sys
from pathlib import Path

from rdflib import Graph, RDF, OWL

REPO_ROOT = Path(__file__).resolve().parent.parent

ONTOLOGY_DIRS = [
    REPO_ROOT / "vital-ontology",
    REPO_ROOT / "domain-ontology",
]


def parse_owl(file_path: Path):
    """Return (ontology_iri, [import_iris]) for an OWL RDF/XML file."""
    g = Graph()
    g.parse(str(file_path), format="application/rdf+xml")

    ont_iri = None
    for s in g.subjects(RDF.type, OWL.Ontology):
        ont_iri = str(s)
        break

    imports = []
    if ont_iri is not None:
        for o in g.objects(None, OWL.imports):
            imports.append(str(o))

    return ont_iri, sorted(imports)


def main() -> int:
    iri_to_file = {}
    iri_to_imports = {}

    for directory in ONTOLOGY_DIRS:
        if not directory.is_dir():
            print(f"WARNING: directory not found: {directory}")
            continue
        for owl_file in sorted(directory.glob("*.owl")):
            ont_iri, imports = parse_owl(owl_file)
            if ont_iri is None:
                print(f"WARNING: no owl:Ontology found in {owl_file}")
                continue
            if ont_iri in iri_to_file:
                print(f"WARNING: duplicate ontology IRI {ont_iri}: "
                      f"{iri_to_file[ont_iri]} and {owl_file}")
            iri_to_file[ont_iri] = owl_file
            iri_to_imports[ont_iri] = imports

    print(f"Found {len(iri_to_file)} ontologies:")
    for iri, path in sorted(iri_to_file.items()):
        print(f"  {iri}  ->  {path.relative_to(REPO_ROOT)}")
    print()

    # walk the closure
    missing = {}  # missing iri -> set of ontologies that need it
    for iri in iri_to_file:
        seen = set()
        stack = [iri]
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            if current not in iri_to_imports:
                missing.setdefault(current, set()).add(iri)
                continue
            stack.extend(iri_to_imports[current])

    # topological order (build order): dependencies first
    order = []
    temp = set()
    done = set()

    def visit(node):
        if node in done or node not in iri_to_imports:
            return
        if node in temp:
            raise RuntimeError(f"Cycle detected involving {node}")
        temp.add(node)
        for dep in iri_to_imports[node]:
            visit(dep)
        temp.discard(node)
        done.add(node)
        order.append(node)

    for iri in sorted(iri_to_file):
        visit(iri)

    print("Topological build order (dependencies first):")
    for i, iri in enumerate(order, 1):
        deps = iri_to_imports.get(iri, [])
        dep_str = f"  (imports: {', '.join(d.rsplit('/', 1)[-1] for d in deps)})" if deps else ""
        print(f"  {i:2}. {iri.rsplit('/', 1)[-1]}{dep_str}")
    print()

    if missing:
        print("MISSING ontologies (IRI not resolvable to a local file):")
        for iri, needed_by in sorted(missing.items()):
            print(f"  {iri}")
            for n in sorted(needed_by):
                print(f"    required by: {n}")
        return 1

    print("Import closure COMPLETE: all owl:imports resolve to local files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
