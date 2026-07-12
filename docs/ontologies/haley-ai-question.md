# haley-ai-question

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/haley-ai-question` |
| **Version** | 0.1.0 |
| **OWL file** | `domain-ontology/haley-ai-question-0.1.0.owl` |
| **Classes** | 267 |
| **Properties** | 766 |
| **Imports** | `haley-taxonomy` |
| **Python package** | [vital-ai-haley-question](https://pypi.org/project/vital-ai-haley-question/) |

## Purpose

Question and answer models: typed questions, answers with constraints
and dependencies, question sets, and their interconnecting edges.

## Key classes

- **`HaleyQuestion`** — a question instance with type, text, options.
- **Typed answers** — `HaleyTextAnswer`, `HaleyChoiceAnswer`,
  `HaleyDateAnswer`, `HaleyNumberAnswer`, `HaleyFileAnswer`, and more.
- **`HaleyAnswerConstraint`** / **`HaleyAnswerDependency`** — validation
  and flow-control logic between questions.
- **`HaleyQuestionSet`** — a grouped collection of questions.
- **Connecting edges** — `Edge_hasAnswer`, `Edge_hasAnswerConstraint`,
  `Edge_hasAnswerDependency`, `Edge_hasAlternateText`, etc.

## Notes

This ontology is imported by `haley-ai-kg`, allowing knowledge graph
frames and slots to reference question/answer structures for data
capture and validation.
