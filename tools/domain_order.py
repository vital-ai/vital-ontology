"""Print the domains from domain-python/domain-config.yaml in dependency
(build) order, derived from owl:imports via the vitalsigns library.

Usage:
    python tools/domain_order.py            # one domain per line, deps first
    python tools/domain_order.py --verbose  # with IRI and direct deps

Intended for driving builds, e.g.:
    for d in $(python tools/domain_order.py); do tools/generate_domain.sh "$d"; done

Fails (exit 1) on unresolvable imports or dependency cycles.
"""

import argparse
import sys
from graphlib import CycleError, TopologicalSorter
from pathlib import Path

import yaml

from vital_ai_vitalsigns_generate.vitalsigns_generator import VitalSignsGenerator

REPO_ROOT = Path(__file__).resolve().parent.parent

ONTOLOGY_DIRS = [
    str(REPO_ROOT / "vital-ontology"),
    str(REPO_ROOT / "domain-ontology"),
]

DOMAIN_CONFIG_PATH = REPO_ROOT / "domain-python" / "domain-config.yaml"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true",
                        help="print IRI and direct dependencies per domain")
    args = parser.parse_args()

    with open(DOMAIN_CONFIG_PATH) as f:
        config = yaml.safe_load(f)

    generator = VitalSignsGenerator()

    iri_to_file = generator.get_iri_to_file_map(ONTOLOGY_DIRS)
    iri_to_imports = generator.get_iri_to_imports_map(ONTOLOGY_DIRS)

    # map each configured domain to its ontology IRI
    domain_to_iri = {}
    for entry in config["domains"]:
        domain = entry["domain"]
        ontology_filename = entry["ontology"]
        owl_path = None
        for directory in ONTOLOGY_DIRS:
            candidate = Path(directory) / ontology_filename
            if candidate.is_file():
                owl_path = candidate
                break
        if owl_path is None:
            print(f"ERROR: ontology file not found for domain {domain}: "
                  f"{ontology_filename}", file=sys.stderr)
            return 1
        domain_to_iri[domain] = generator.extract_iri_from_owl(str(owl_path))

    iri_to_domain = {iri: d for d, iri in domain_to_iri.items()}

    # check that every import in the closure resolves to a local OWL file
    missing = set()
    for iri in domain_to_iri.values():
        stack = [iri]
        seen = set()
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            if current not in iri_to_imports:
                missing.add(current)
                continue
            stack.extend(iri_to_imports[current])
    if missing:
        for iri in sorted(missing):
            print(f"ERROR: unresolvable owl:import: {iri}", file=sys.stderr)
        return 1

    # build the domain-level dependency graph: domain -> set of domains whose
    # ontologies appear in its (transitive) import closure
    graph = {}
    for domain, iri in domain_to_iri.items():
        deps = set()
        stack = list(iri_to_imports[iri])
        seen = set()
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            dep_domain = iri_to_domain.get(current)
            if dep_domain is not None and dep_domain != domain:
                deps.add(dep_domain)
            stack.extend(iri_to_imports.get(current, []))
        graph[domain] = deps

    try:
        order = list(TopologicalSorter(graph).static_order())
    except CycleError as e:
        print(f"ERROR: dependency cycle: {e.args[1]}", file=sys.stderr)
        return 1

    for domain in order:
        if args.verbose:
            direct = sorted(
                iri_to_domain[i] for i in iri_to_imports[domain_to_iri[domain]]
                if i in iri_to_domain)
            print(f"{domain}  iri={domain_to_iri[domain]}  deps={direct}")
        else:
            print(domain)

    return 0


if __name__ == "__main__":
    sys.exit(main())
