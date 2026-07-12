# vital-wordnet

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/vital-wordnet` |
| **Version** | 0.2.304 |
| **OWL file** | `domain-ontology/vital-wordnet-0.2.304.owl` |
| **Classes** | 33 |
| **Properties** | 4 |
| **Imports** | `vital` |
| **Python package** | [vital-ai-wordnet](https://pypi.org/project/vital-ai-wordnet/) |

## Purpose

WordNet lexical database models: synsets organized by part of speech
and their lexical relation edges.

## Key classes

- **`SynsetNode`** — abstract synset base, with subtypes:
  `NounSynsetNode`, `VerbSynsetNode`, `AdjectiveSynsetNode`,
  `AdverbSynsetNode`.
- **Relation edges** — `Edge_WordnetHypernym`, `Edge_WordnetHyponym`,
  `Edge_WordnetAntonym`, `Edge_WordnetMeronym`, `Edge_WordnetHolonym`,
  `Edge_WordnetAlsoSee`, `Edge_WordnetAttribute`, and others.

## Notes

This is a relatively small ontology (33 classes, 4 own properties);
the bulk of the data is in the synset node/edge instances loaded from
the WordNet corpus.
