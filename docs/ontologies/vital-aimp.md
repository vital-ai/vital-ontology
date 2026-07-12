# vital-aimp

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/vital-aimp` |
| **Version** | 0.1.0 |
| **OWL file** | `domain-ontology/vital-aimp-0.1.0.owl` |
| **Classes** | 699 |
| **Properties** | 1,328 |
| **Imports** | `vital`, `vital-social`, `vital-nlp` |
| **Python package** | [vital-ai-aimp](https://pypi.org/project/vital-ai-aimp/) |

## Purpose

The **AI Message Protocol (AIMP)** — the message schema for
communication between Vital AI agents, applications, and channels.
This is one of the largest ontologies by class count.

## Key classes

- **`AIMPMessage`** — base message exchanged between agents.
- **`AIMPCommand`** / **`AIMPCommandMessage`** — command messages with
  typed operation and command types.
- **`AIMPDevice`** — device context for sessions.
- **`AIMPEmailMessage`** — email-channel messages.
- **`AIMPIntent`** / **`AIMPIntentMessage`** — intent-based interactions.
- **Cards** — `TextCard`, `ImageCard`, `VideoCard`, `FileCard`,
  `ChoiceCard`, `FormCard`, `PanelCard`, and many more UI card types.
- **Payloads** — various typed payloads for rich interactions.

## Notes

AIMP is the protocol layer; higher-level domains (haley, chat-ai) build
application semantics on top of it. The large class/property count
reflects the richness of the messaging protocol.
