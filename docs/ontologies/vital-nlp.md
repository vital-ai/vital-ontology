# vital-nlp

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/vital-nlp` |
| **Version** | 0.2.304 |
| **OWL file** | `domain-ontology/vital-nlp-0.2.304.owl` |
| **Classes** | 55 |
| **Properties** | 166 |
| **Imports** | `vital` |
| **Python package** | [vital-ai-nlp](https://pypi.org/project/vital-ai-nlp/) |

## Purpose

Natural language processing models: documents, annotations, and their
structural parts.

## Key classes

- **`Document`** — a text document with body/title/metadata.
- **`Sentence`** / **`TextBlock`** — structural segments.
- **`Annotation`** / **`EntityInstance`** — NLP annotations (tokens,
  entities, parts of speech).
- **`Abbreviation`** / **`AbbreviationInstance`** — abbreviation handling.
- **`Content`** — raw content container.
