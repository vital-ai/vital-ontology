# vital-ontology

Source of truth for the Vital AI OWL ontologies and the python domain
packages generated from them. The ontologies define the classes and
properties of the Vital AI knowledge graph; the generated packages provide
python bindings used with
[vital-ai-vitalsigns](https://pypi.org/project/vital-ai-vitalsigns/).

All domain packages are generated, versioned, and published to PyPI from
this repository.

## Repository layout

| Path | Contents |
|---|---|
| `vital-ontology/` | Foundation OWL files: `vital-core` and `vital` |
| `domain-ontology/` | Domain OWL files (plus `archive/` of older revisions) |
| `vital-domain-python/` | The `vital-ai-domain` package (bindings for `vital`) |
| `domain-python/` | The 10 domain packages, one directory each |
| `domain-python/domain-config.yaml` | Domain list consumed by the generator |
| `tools/` | Generation / comparison / ordering helper scripts |
| `tests/` | Functionality test suite run against the published packages |
| `vitalhome/` | Repo-local VITAL_HOME config used by the vitalsigns CLI |
| `docs/` | GitBook documentation |

Note: `vital-core` python bindings (`vital_ai_vitalsigns_core`) are bundled
inside the `vital-ai-vitalsigns` package, which is maintained in
[vital-vitalsigns-python](https://github.com/vital-ai/vital-vitalsigns-python).

## Packages

In dependency (build) order, computed from `owl:imports` (`make order`):

| Package dir | PyPI package | Ontology IRI |
|---|---|---|
| `vital-domain-python` | [vital-ai-domain](https://pypi.org/project/vital-ai-domain/) | `http://vital.ai/ontology/vital` |
| `vital-nlp-python` | [vital-ai-nlp](https://pypi.org/project/vital-ai-nlp/) | `http://vital.ai/ontology/vital-nlp` |
| `vital-wordnet-python` | [vital-ai-wordnet](https://pypi.org/project/vital-ai-wordnet/) | `http://vital.ai/ontology/vital-wordnet` |
| `vital-social-python` | [vital-ai-social](https://pypi.org/project/vital-ai-social/) | `http://vital.ai/ontology/vital-social` |
| `vital-aimp-python` | [vital-ai-aimp](https://pypi.org/project/vital-ai-aimp/) | `http://vital.ai/ontology/vital-aimp` |
| `haley-python` | [vital-ai-haley](https://pypi.org/project/vital-ai-haley/) | `http://vital.ai/ontology/haley` |
| `haley-taxonomy-python` | [vital-ai-haley-taxonomy](https://pypi.org/project/vital-ai-haley-taxonomy/) | `http://vital.ai/ontology/haley-taxonomy` |
| `haley-ai-question-python` | [vital-ai-haley-question](https://pypi.org/project/vital-ai-haley-question/) | `http://vital.ai/ontology/haley-ai-question` |
| `haley-ai-kg-python` | [vital-ai-haley-kg](https://pypi.org/project/vital-ai-haley-kg/) | `http://vital.ai/ontology/haley-ai-kg` |
| `haley-ai-ml-python` | [vital-ai-haley-ml](https://pypi.org/project/vital-ai-haley-ml/) | `http://vital.ai/ontology/haley-ai-ml` |
| `chat-ai-python` | [vital-ai-chat](https://pypi.org/project/vital-ai-chat/) | `http://vital.ai/ontology/chat-ai` |

Installing a package pulls its ontology parents automatically, e.g.
`pip install vital-ai-chat` installs the full chain.

Besides the core, the most important ontology is **haley-ai-kg**
(`vital-ai-haley-kg`): it defines the core knowledge graph representation
models, including the `KGEntity`, `KGFrame`, and `KGSlot` classes (and
their type hierarchies and connecting edges) used to represent entities,
frames, and slot values in the Vital AI knowledge graph.

## Quick start

```bash
conda env create -f environment.yml
conda activate vital-ontology
make help
```

Main targets:

| Target | Purpose |
|---|---|
| `make order` | Print domains in dependency order (from `owl:imports`) |
| `make check-imports` | Verify the `owl:imports` closure is complete |
| `make generate` | Generate all domains via the `vitalsigns` CLI into `build/generated/` |
| `make verify` | Generate + diff against the committed packages (CI gate) |
| `make test` | Run the functionality test suite (`tests/`) |
| `make build` | Build sdist+wheel for all packages in dependency order |
| `make test-install` | Install built wheels into a fresh venv and smoke-test imports |
| `make publish` | Upload to PyPI in dependency order (`--skip-existing`) |

## Development workflow

Generated code is never edited by hand. To change a domain:

1. Edit the OWL file (`domain-ontology/` or `vital-ontology/`); bump its
   `owl:versionInfo`.
2. `make generate` then `make verify-<domain>` to review the diff.
3. Copy the regenerated output into the committed package tree.
4. Bump versions per the cascading policy: the changed package bumps, and
   every downstream package bumps too, raising its dependency floor on the
   changed parent (dependents are computed from the same `owl:imports`
   graph as `make order`).
5. `make build && make test-install && make test`, then `make publish`.

Changes to `vital-core` are made in
[vital-vitalsigns-python](https://github.com/vital-ai/vital-vitalsigns-python)
(and its OWL copy here is synced afterwards); a vitalsigns release then
precedes the domain package releases.

## Documentation

Full documentation lives in [`docs/`](docs/README.md) (GitBook).

## License

Apache License 2.0 — applies to this repository and all generated packages
(see `LICENSE` here and in each package directory).
