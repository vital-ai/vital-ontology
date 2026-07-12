# Vital Ontology

The **Vital AI Ontology** is a suite of 12 OWL ontologies that define
the classes and properties of the Vital AI knowledge graph platform.
This repository serves as the source of truth for both the ontologies
and the python domain packages generated from them.

## What is this?

Vital AI uses a typed, schema-driven knowledge graph. Every object in
the system — entities, frames, messages, documents, accounts — is an
instance of an OWL class with declared properties. The ontologies
define the schema; the generated python packages provide runtime
bindings used with
[vital-ai-vitalsigns](https://pypi.org/project/vital-ai-vitalsigns/).

## The ontology stack

```
vital-core          ← foundation (types, edges, nodes, properties)
  └─ vital          ← general-purpose domain (accounts, files, …)
       ├─ vital-nlp         (NLP annotations, documents)
       │    └─ vital-wordnet (WordNet synsets)
       ├─ vital-social      (social media, campaigns)
       └─ vital-aimp        (AI Message Protocol)
            └─ haley         (Haley platform: agents, apps, channels)
                 ├─ haley-taxonomy  (category taxonomy)
                 │    └─ haley-ai-question (Q&A models)
                 │         └─ haley-ai-kg   ← core KG models
                 ├─ haley-ai-ml     (ML intents, features, prompts)
                 └─ chat-ai         (chat application messages)
```

The most important ontology besides the core is **haley-ai-kg** — it
defines the knowledge graph representation (`KGEntity`, `KGFrame`,
`KGSlot`) used throughout the platform.

## Quick links

- [Ontologies overview](ontologies/overview.md) — the 12 ontologies with
  class/property counts and the imports graph.
- [Python packages](packages/overview.md) — PyPI names, install, and
  dependency chain.
- [Using the packages](packages/usage.md) — create objects, set
  properties, serialize.
- [Development](development/layout.md) — repository layout, generation
  pipeline, release process, and testing.
