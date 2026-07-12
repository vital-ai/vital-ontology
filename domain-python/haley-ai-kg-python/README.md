# vital-ai-haley-kg

Python bindings for the **haley-ai-kg** ontology
(`http://vital.ai/ontology/haley-ai-kg`, version 0.1.0) — the core
knowledge graph representation models of the Vital AI platform. Besides
`vital-core`, this is the most important ontology in the stack.

## Knowledge graph model

The central classes:

- **`KGEntity`** — a node representing an entity in the knowledge graph
  (a person, place, product, concept, …), typed via `hasKGEntityType`.
- **`KGFrame`** — a frame grouping a set of slot values that together
  describe a fact, event, or structured record about entities.
- **`KGSlot`** — a slot within a frame holding a single typed value, with
  typed subclasses per datatype (`KGTextSlot`, `KGIntegerSlot`,
  `KGDoubleSlot`, `KGBooleanSlot`, `KGDateTimeSlot`, `KGEntitySlot`,
  `KGChoiceSlot`, and others).

Entities, frames, and slots are connected with edges such as
`Edge_hasKGFrame`, `Edge_hasKGSlot`, and `Edge_hasKGRelation`, allowing
frames to describe single entities or relate multiple entities. The
ontology also includes supporting models for KG documents, queries, agents,
tools, chat interactions, and provenance types.

## Install

```bash
pip install vital-ai-haley-kg
```

Direct dependencies: `vital-ai-haley`, `vital-ai-haley-question`.

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from ai_haley_kg_domain.model.KGEntity import KGEntity
from ai_haley_kg_domain.model.KGFrame import KGFrame
from ai_haley_kg_domain.model.KGTextSlot import KGTextSlot
from ai_haley_kg_domain.model.Edge_hasKGFrame import Edge_hasKGFrame
from ai_haley_kg_domain.model.Edge_hasKGSlot import Edge_hasKGSlot

vs = VitalSigns()

entity = KGEntity()
entity.URI = 'http://example.org/kg/entity-1'
entity.name = 'Example Entity'
entity.kGEntityTypeDescription = 'an example entity'

frame = KGFrame()
frame.URI = 'http://example.org/kg/frame-1'

slot = KGTextSlot()
slot.URI = 'http://example.org/kg/slot-1'
slot.textSlotValue = 'example value'

entity_frame = Edge_hasKGFrame()
entity_frame.URI = 'http://example.org/kg/edge-1'
entity_frame.edgeSource = entity.URI
entity_frame.edgeDestination = frame.URI

frame_slot = Edge_hasKGSlot()
frame_slot.URI = 'http://example.org/kg/edge-2'
frame_slot.edgeSource = frame.URI
frame_slot.edgeDestination = slot.URI

for obj in (entity, frame, slot, entity_frame, frame_slot):
    print(obj.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
