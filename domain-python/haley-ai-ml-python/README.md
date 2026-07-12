# vital-ai-haley-ml

Python bindings for the **haley-ai-ml** ontology
(`http://vital.ai/ontology/haley-ai-ml`, version 0.1.0) — machine learning
models: intents and intent slots, features and feature values, prediction
and recommendation models, prompts, and mind/inference requests.

## Install

```bash
pip install vital-ai-haley-ml
```

Direct dependency: `vital-ai-haley`.

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from ai_haley_ml_domain.model.HaleyIntent import HaleyIntent

vs = VitalSigns()

intent = HaleyIntent()
intent.URI = 'http://example.org/ml/intent-1'
intent.name = 'Example Intent'

print(intent.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
