# vital-ai-wordnet

Python bindings for the **vital-wordnet** ontology
(`http://vital.ai/ontology/vital-wordnet`, version 0.2.304) — WordNet
lexical models: synset nodes per part of speech (noun, verb, adjective,
adverb) and the WordNet relation edges (hypernym, hyponym, antonym,
meronym, and the rest).

## Install

```bash
pip install vital-ai-wordnet
```

Direct dependency: `vital-ai-domain` (which brings in
`vital-ai-vitalsigns`).

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from com_vitalai_domain_wordnet.model.NounSynsetNode import NounSynsetNode

vs = VitalSigns()

synset = NounSynsetNode()
synset.URI = 'http://example.org/wordnet/synset-1'
synset.name = 'example'

print(synset.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
