# Ontologies overview

The Vital AI platform is built on 12 OWL ontologies arranged in a single
`owl:imports` tree. Each ontology defines a domain of classes and
properties; downstream ontologies inherit from upstream ones.

## The 12 ontologies

| Ontology | OWL IRI | Version | Classes | Properties |
|---|---|---|---|---|
| [vital-core](vital-core.md) | `http://vital.ai/ontology/vital-core` | 0.2.304 | 63 | 172 |
| [vital](vital.md) | `http://vital.ai/ontology/vital` | 0.2.304 | 57 | 116 |
| [vital-nlp](vital-nlp.md) | `http://vital.ai/ontology/vital-nlp` | 0.2.304 | 55 | 166 |
| [vital-wordnet](vital-wordnet.md) | `http://vital.ai/ontology/vital-wordnet` | 0.2.304 | 33 | 4 |
| [vital-social](vital-social.md) | `http://vital.ai/ontology/vital-social` | 0.2.304 | 33 | 136 |
| [vital-aimp](vital-aimp.md) | `http://vital.ai/ontology/vital-aimp` | 0.1.0 | 699 | 1328 |
| [haley](haley.md) | `http://vital.ai/ontology/haley` | 0.1.0 | 305 | 732 |
| [haley-taxonomy](haley-taxonomy.md) | `http://vital.ai/ontology/haley-taxonomy` | 0.1.0 | 5 | 8 |
| [haley-ai-question](haley-ai-question.md) | `http://vital.ai/ontology/haley-ai-question` | 0.1.0 | 267 | 766 |
| [haley-ai-kg](haley-ai-kg.md) | `http://vital.ai/ontology/haley-ai-kg` | 0.1.0 | 332 | 781 |
| [haley-ai-ml](haley-ai-ml.md) | `http://vital.ai/ontology/haley-ai-ml` | 0.1.0 | 43 | 92 |
| [chat-ai](chat-ai.md) | `http://vital.ai/ontology/chat-ai` | 0.1.0 | 497 | 718 |

**Total**: ~2,389 classes, ~5,019 properties across all ontologies.

## Imports graph

```
vital-core
  └─ vital
       ├─ vital-nlp
       │    └─ vital-wordnet
       ├─ vital-social (imports: vital, vital-nlp)
       └─ vital-aimp (imports: vital, vital-social, vital-nlp)
            └─ haley
                 ├─ haley-taxonomy
                 │    └─ haley-ai-question
                 │         └─ haley-ai-kg (imports: haley, haley-ai-question)
                 ├─ haley-ai-ml
                 └─ chat-ai (imports: haley, haley-ai-kg, haley-ai-ml, vital-aimp)
```

All ontologies are rooted in `vital-core`. Installing the leaf package
(`vital-ai-chat`) transitively installs bindings for the entire tree.

## Key ontology

The most important domain ontology is **haley-ai-kg**: it defines the
core knowledge graph representation — `KGEntity`, `KGFrame`, `KGSlot`
— used to store structured knowledge throughout the platform. See
the [haley-ai-kg page](haley-ai-kg.md) for details.
