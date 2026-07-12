# haley-taxonomy

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/haley-taxonomy` |
| **Version** | 0.1.0 |
| **OWL file** | `domain-ontology/haley-taxonomy-0.1.0.owl` |
| **Classes** | 5 |
| **Properties** | 8 |
| **Imports** | `haley` |
| **Python package** | [vital-ai-haley-taxonomy](https://pypi.org/project/vital-ai-haley-taxonomy/) |

## Purpose

A small ontology for representing **category taxonomies** — hierarchical
classification structures used for knowledge organization.

## Key classes

- **`TaxonomyNode`** — a category node in the taxonomy.
- **Category edges** — `Edge_hasBroaderCategory`,
  `Edge_hasNarrowerCategory`, `Edge_hasRelatedCategory`,
  `Edge_hasEquivalentCategory`.

## Notes

Despite its small class count, this ontology is structurally important:
`haley-ai-question` imports it, giving questions access to taxonomy-based
answer choices and categories.
