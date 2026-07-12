# vital

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/vital` |
| **Version** | 0.2.304 |
| **OWL file** | `vital-ontology/vital-0.2.304.owl` |
| **Classes** | 57 |
| **Properties** | 116 |
| **Imports** | `vital-core` |
| **Python package** | [vital-ai-domain](https://pypi.org/project/vital-ai-domain/) |

## Purpose

The general-purpose Vital AI domain, layered directly on `vital-core`.
Defines widely shared application-level classes and their connecting
edges.

## Key classes

- **`Account`** — user account with login, settings, and access URIs.
- **`Login`** / **`CredentialsLogin`** / **`AdminLogin`** — authentication.
- **`FileNode`** — uploaded/generated file metadata.
- **`DatascriptInfo`** / **`DatascriptRun`** — data scripts and execution.
- **`Job`** — asynchronous job tracking.
- **`Event`** — timestamped events.
- **`BusinessOrganization`** — organization entities.
- **`VitalOntNode`** / **`VitalOntEdge`** — ontology metadata objects
  (added 2026-07).

## Notes

This is the root of the domain package tree — all other domain packages
depend on it. Its `owl:imports` brings in `vital-core`, so installing
`vital-ai-domain` also installs `vital-ai-vitalsigns`.
