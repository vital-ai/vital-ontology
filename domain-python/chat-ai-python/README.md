# vital-ai-chat

Python bindings for the **chat-ai** ontology
(`http://vital.ai/ontology/chat-ai`, version 0.1.0) — the chat application
domain: chat requests/responses, account and member administration,
notifications, payments, quotas, and the other message types exchanged by
the Vital AI chat applications. This is the leaf of the domain package
chain; installing it pulls in every other Vital AI domain package.

## Install

```bash
pip install vital-ai-chat
```

Direct dependencies: `vital-ai-domain`, `vital-ai-haley`,
`vital-ai-haley-kg`, `vital-ai-haley-ml`, `vital-ai-aimp`.

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from ai_chat_domain.model.AIMPMessageMetaInfo import AIMPMessageMetaInfo

vs = VitalSigns()

meta = AIMPMessageMetaInfo()
meta.URI = 'http://example.org/chat/meta-1'
meta.name = 'Example Meta Info'

print(meta.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
