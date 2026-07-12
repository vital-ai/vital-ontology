# haley-ai-kg

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/haley-ai-kg` |
| **Version** | 0.1.0 |
| **OWL file** | `domain-ontology/haley-ai-kg-0.1.0.owl` |
| **Classes** | 332 |
| **Properties** | 781 |
| **Imports** | `haley`, `haley-ai-question` |
| **Python package** | [vital-ai-haley-kg](https://pypi.org/project/vital-ai-haley-kg/) |

## Purpose

The **core knowledge graph representation** ontology — besides
`vital-core`, this is the most important ontology in the Vital AI
stack. It defines the Entity–Frame–Slot model used to represent
structured knowledge throughout the platform.

## The Entity–Frame–Slot model

The central pattern:

```
KGEntity ──Edge_hasKGFrame──▶ KGFrame ──Edge_hasKGSlot──▶ KGSlot
```

- **`KGEntity`** — an entity (person, place, product, concept, …),
  typed by `hasKGEntityType`. Entities are the "nouns" of the knowledge
  graph.
- **`KGFrame`** — a frame describing a fact, event, or structured record
  about one or more entities. Frames are the "verbs" or "relations."
- **`KGSlot`** — a single typed value within a frame. Subclasses per
  datatype:
  - `KGTextSlot` — string values
  - `KGIntegerSlot` / `KGDoubleSlot` — numeric values
  - `KGBooleanSlot` — true/false
  - `KGDateTimeSlot` — timestamps
  - `KGEntitySlot` — references to other entities
  - `KGChoiceSlot` — enumerated choices
  - And others for specialized value types.

## Key edges

- **`Edge_hasKGFrame`** — connects an entity to its frames.
- **`Edge_hasKGSlot`** — connects a frame to its slots.
- **`Edge_hasKGRelation`** — inter-entity relations within the KG.
- **`Edge_hasActorKGFrame`** / **`Edge_hasAgentKGFrame`** /
  **`Edge_hasChatMessageKGFrame`** / **`Edge_hasDocumentKGFrame`** —
  specialized frame edges for different contexts.

## Supporting models

Beyond Entity–Frame–Slot, the ontology includes:

- **KG documents and queries** — classes for document-backed knowledge.
- **KG agents and tools** — agent interaction within the KG context.
- **Provenance types** — tracking the origin and confidence of KG data.
- **Domain categories** — classification within the KG.

## Usage example

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from ai_haley_kg_domain.model.KGEntity import KGEntity
from ai_haley_kg_domain.model.KGFrame import KGFrame
from ai_haley_kg_domain.model.KGTextSlot import KGTextSlot
from ai_haley_kg_domain.model.Edge_hasKGFrame import Edge_hasKGFrame
from ai_haley_kg_domain.model.Edge_hasKGSlot import Edge_hasKGSlot

vs = VitalSigns()

# Create an entity
entity = KGEntity()
entity.URI = 'urn:example:entity-1'
entity.name = 'Vital AI'
entity.kGEntityTypeDescription = 'company'

# Create a frame describing a fact about the entity
frame = KGFrame()
frame.URI = 'urn:example:frame-1'

# Create a slot with a text value
slot = KGTextSlot()
slot.URI = 'urn:example:slot-1'
slot.textSlotValue = 'San Francisco'

# Wire them together
e2f = Edge_hasKGFrame()
e2f.URI = 'urn:example:edge-1'
e2f.edgeSource = entity.URI
e2f.edgeDestination = frame.URI

f2s = Edge_hasKGSlot()
f2s.URI = 'urn:example:edge-2'
f2s.edgeSource = frame.URI
f2s.edgeDestination = slot.URI
```
