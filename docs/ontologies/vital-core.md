# vital-core

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/vital-core` |
| **Version** | 0.2.304 |
| **OWL file** | `vital-ontology/vital-core-0.2.304.owl` |
| **Classes** | 63 |
| **Properties** | 172 |
| **Imports** | _(root — no imports)_ |
| **Python package** | Bundled in [vital-ai-vitalsigns](https://pypi.org/project/vital-ai-vitalsigns/) (`vital_ai_vitalsigns_core`) |

## Purpose

The foundation ontology. Defines the abstract superclasses that every
object in the system extends:

- **`VITAL_Node`** — the base graph node.
- **`VITAL_Edge`** — directed typed edges connecting nodes.
- **`VITAL_HyperNode`** / **`VITAL_HyperEdge`** — for multi-endpoint
  relations.
- **`VITAL_GraphContainerObject`** — container semantics.

Also declares the universal property traits used across all domains
(URI, name, timestamp, active flag, provenance, etc.) and service
configuration classes (`VitalServiceConfig`, `VitalServiceSqlConfig`).

## Key classes

`VITAL_Node`, `VITAL_Edge`, `VITAL_HyperNode`, `VITAL_HyperEdge`,
`VITAL_GraphContainerObject`, `VitalServiceConfig`,
`VitalServiceSqlConfig`, `VitalSegment`, `VitalApp`.

## Notes

This ontology's python bindings ship inside `vital-ai-vitalsigns` (not
as a separate PyPI package). Changes are made in the
[vital-vitalsigns-python](https://github.com/vital-ai/vital-vitalsigns-python)
repository; the OWL copy here is kept in sync.
