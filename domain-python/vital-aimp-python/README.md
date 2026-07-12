# vital-ai-aimp

Python bindings for the **vital-aimp** ontology
(`http://vital.ai/ontology/vital-aimp`, version 0.1.0) — the AIMP (AI
Message Protocol) models: messages, commands, payloads, devices, channels,
intents, and cards used for messaging between Vital AI agents and
applications.

## Install

```bash
pip install vital-ai-aimp
```

Direct dependencies: `vital-ai-domain`, `vital-ai-social`, `vital-ai-nlp`.

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage

vs = VitalSigns()

message = AIMPMessage()
message.URI = 'http://example.org/aimp/message-1'
message.name = 'Example AIMP Message'

print(message.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
