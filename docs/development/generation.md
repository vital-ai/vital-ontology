# Generation pipeline

The python domain packages are **generated** from the OWL ontologies —
they are never edited by hand. The generation is driven by the
`vitalsigns` CLI (from `vital-ai-vitalsigns>=0.1.54`) and orchestrated
via Make targets.

## How it works

```
OWL file → vitalsigns generate → python package tree
```

For each domain, the generator:

1. Reads the OWL file and its transitive `owl:imports`.
2. Emits one python class per `owl:Class` (under `model/`), with
   `_allowed_properties` populated from declared
   `owl:DatatypeProperty` / `owl:ObjectProperty` entries.
3. Emits one property trait class per property (under
   `model/properties/`).
4. Emits type stubs (`.pyi`) for IDE autocompletion.
5. Produces the domain ontology metadata class (`DomainOntology.py`).
6. Bundles the OWL file itself inside the package (under
   `domain-ontology/` or `vital-ontology/`).

## Running generation

```bash
# Generate all domains (into build/generated/):
make generate

# Generate one domain:
make generate-haley-ai-kg-python

# Generate + diff against committed code (parity check):
make verify
make verify-haley-ai-kg-python
```

`make generate` writes output to `build/generated/<domain>/` —
it does NOT overwrite the committed packages. After reviewing the diff
(`make verify`), you adopt the changes manually.

## Dependency order

Domains must be generated in topological order (parents before children)
because the generator resolves parent classes. The order is computed from
`owl:imports` by `tools/domain_order.py`:

```bash
make order
# Output: vital-domain-python vital-nlp-python vital-wordnet-python
#         vital-social-python vital-aimp-python haley-python
#         haley-taxonomy-python haley-ai-question-python
#         haley-ai-kg-python haley-ai-ml-python chat-ai-python
```

## Configuration

- **`domain-python/domain-config.yaml`** — lists all domain packages
  with their OWL file, output directory, and package module name.
- **`tools/generate_domain.sh`** — the per-domain wrapper that invokes
  `vitalsigns generate` with the correct arguments.
- **`vital_env.env`** / **`vitalhome/`** — provides the VITAL_HOME
  context the generator needs.

## Parity checking

`make verify` is the CI gate: it regenerates every domain and diffs the
output against the committed package tree. If there is any divergence,
the check fails — indicating either the OWL was edited without
regenerating, or the generator has a behavior change.
