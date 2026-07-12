# haley

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/haley` |
| **Version** | 0.1.0 |
| **OWL file** | `domain-ontology/haley-0.1.0.owl` |
| **Classes** | 305 |
| **Properties** | 732 |
| **Imports** | `vital-aimp` |
| **Python package** | [vital-ai-haley](https://pypi.org/project/vital-ai-haley/) |

## Purpose

The **Haley platform** domain: accounts, sessions, agents, apps,
channels, deployments, bots, and platform infrastructure.

## Key classes

- **`CloudAgent`** — a deployed AI agent.
- **`CloudApp`** / **`CloudAppDeployment`** — applications and their
  deployment metadata.
- **`CloudBucket`** — storage bucket definitions.
- **`HaleyAPIKey`** — API key management.
- **`HaleyAccountGroup`** / **`HaleyAccountOffice`** — organizational
  groupings.
- **`AgentDeveloper`** — developer accounts.
- **`ChannelOrgType`** — channel type definitions.

## Notes

This is the platform "backbone" ontology that the AI-specific ontologies
(taxonomy, question, kg, ml, chat) extend.
