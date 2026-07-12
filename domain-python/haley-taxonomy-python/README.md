# vital-ai-haley-taxonomy

Python bindings for the **haley-taxonomy** ontology
(`http://vital.ai/ontology/haley-taxonomy`, version 0.1.0) — taxonomy
models: taxonomy nodes and the broader/narrower/related/equivalent category
edges used to organize categories across the Haley platform.

## Install

```bash
pip install vital-ai-haley-taxonomy
```

Direct dependency: `vital-ai-haley`.

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from com_vitalai_haley_taxonomy_domain.model.TaxonomyNode import TaxonomyNode

vs = VitalSigns()

node = TaxonomyNode()
node.URI = 'http://example.org/taxonomy/node-1'
node.name = 'Example Category'

print(node.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
