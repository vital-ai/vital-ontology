# vital-ai-nlp

Python bindings for the **vital-nlp** ontology
(`http://vital.ai/ontology/vital-nlp`, version 0.2.304) — natural language
processing models: documents, sentences, token/tag annotations, entities and
entity instances, abbreviations, and related NLP artifacts.

## Install

```bash
pip install vital-ai-nlp
```

Direct dependency: `vital-ai-domain` (which brings in
`vital-ai-vitalsigns`).

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from com_vitalai_domain_nlp.model.Document import Document

vs = VitalSigns()

doc = Document()
doc.URI = 'http://example.org/document/1'
doc.name = 'Example Document'

print(doc.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
