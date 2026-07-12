# Using the packages

## Initialization

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns

# Singleton — discovers all installed domain packages on first call.
# Builds the class/property registry (~14s cold, <1s cached).
vs = VitalSigns()
```

`VitalSigns()` scans all `vitalsigns_packages` entry points, imports
their modules, and builds a registry mapping class URIs to python
classes and property URIs to property traits.

## Creating objects

Every OWL class has a corresponding python class with:

- A `URI` attribute (required — every graph object has a unique URI).
- A `name` attribute (inherited from `vital-core`).
- Domain-specific properties declared in `_allowed_properties`.

```python
from ai_haley_kg_domain.model.KGEntity import KGEntity

entity = KGEntity()
entity.URI = 'urn:example:entity-1'
entity.name = 'Example Entity'
entity.kGEntityTypeDescription = 'a person'
```

## Setting properties

Properties can be set by short name (attribute access) or by full URI:

```python
# By short name (camelCase, derived from the property URI fragment):
entity.kGEntityTypeDescription = 'a person'

# By full URI via set_property / get_property_value:
entity.set_property(
    'http://vital.ai/ontology/haley-ai-kg#hasKGEntityTypeDescription',
    'a person')

value = entity.get_property_value(
    'http://vital.ai/ontology/haley-ai-kg#hasKGEntityTypeDescription')
```

Setting a property not declared in the class's `_allowed_properties`
(nor inherited) raises `AttributeError`.

## Multi-valued properties

Some properties accept multiple values (declared with
`multiple_values = True` on the property trait):

```python
from vital_ai_domain.model.Account import Account

account = Account()
account.URI = 'urn:example:account-1'
account.accountAccessURIs = [
    'urn:example:access-1',
    'urn:example:access-2',
]
# Returns a list:
print(account.accountAccessURIs)
```

## Edges

Edges connect nodes with source/destination URIs:

```python
from ai_haley_kg_domain.model.Edge_hasKGFrame import Edge_hasKGFrame

edge = Edge_hasKGFrame()
edge.URI = 'urn:example:edge-1'
edge.edgeSource = 'urn:example:entity-1'
edge.edgeDestination = 'urn:example:frame-1'
```

## Serialization

Every graph object supports multiple serialization formats:

```python
from vital_ai_vitalsigns.model.GraphObject import GraphObject

# JSON (the primary wire format):
json_str = entity.to_json()
restored = GraphObject.from_json(json_str)  # polymorphic — resolves class

# RDF (N-Triples):
rdf_str = entity.to_rdf()
restored = GraphObject.from_rdf(rdf_str)

# Python dict:
d = entity.to_dict()
restored = GraphObject.from_dict(d)

# JSON-LD:
jsonld = entity.to_jsonld()
restored = GraphObject.from_jsonld(jsonld)

# Triples (list of (s, p, o) tuples):
triples = entity.to_triples()
```

`GraphObject.from_json()` uses the registry to resolve the type URI in
the JSON to the correct python class — no need to know the class ahead
of time.

## Block files

For bulk data, use the `.vital` block format:

```python
from vital_ai_vitalsigns.block.vital_block import VitalBlock
from vital_ai_vitalsigns.block.vital_block_file import VitalBlockFile
from vital_ai_vitalsigns.block.vital_block_reader import VitalBlockReader
from vital_ai_vitalsigns.block.vital_block_writer import VitalBlockWriter

# Write
writer = VitalBlockWriter(
    VitalBlockFile('data.vital'),
    encoding='jsonl',
    version='1.0.0',
    ontologies=[],
    metadata={},
)
writer.write_header()
writer.write_block(VitalBlock([entity, edge, frame]))
writer.close()

# Read
for block in VitalBlockReader(VitalBlockFile('data.vital')):
    objects = [block.first_object] + block.rest_objects
    for obj in objects:
        print(type(obj).__name__, obj.URI)
```

## Class URI resolution

To look up a class by its ontology URI at runtime:

```python
registry = vs.get_registry()
cls = registry.get_vitalsigns_class(
    'http://vital.ai/ontology/haley-ai-kg#KGEntity')
entity = cls()  # same as KGEntity()
```
