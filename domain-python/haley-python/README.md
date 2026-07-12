# vital-ai-haley

Python bindings for the **haley** ontology
(`http://vital.ai/ontology/haley`, version 0.1.0) — the Haley platform
domain: accounts, groups, sessions, cloud apps/agents/deployments, channels,
bots, and platform infrastructure models.

## Install

```bash
pip install vital-ai-haley
```

Direct dependency: `vital-ai-aimp` (which brings in the rest of the chain
down to `vital-ai-vitalsigns`).

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from com_vitalai_haley_domain.model.CloudAgent import CloudAgent

vs = VitalSigns()

agent = CloudAgent()
agent.URI = 'http://example.org/haley/agent-1'
agent.name = 'Example Agent'

print(agent.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
