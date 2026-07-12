# vital-ai-social

Python bindings for the **vital-social** ontology
(`http://vital.ai/ontology/vital-social`, version 0.2.304) — social media
models: posts, direct messages, user profiles, campaigns and campaign
actions, and related social graph edges.

## Install

```bash
pip install vital-ai-social
```

Direct dependencies: `vital-ai-domain`, `vital-ai-nlp`.

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from com_vitalai_domain_social.model.DirectMessage import DirectMessage

vs = VitalSigns()

message = DirectMessage()
message.URI = 'http://example.org/social/message-1'
message.name = 'Example Message'

print(message.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
