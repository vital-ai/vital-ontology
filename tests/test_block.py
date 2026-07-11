"""Area 5: block format / bulk data (domain-testing-plan.md).

Writes a heterogeneous .vital block file with objects from several domains
and reads it back (cf. vitalsigns test_scripts/block/test_block_read_write.py).
"""

import os

from vital_ai_vitalsigns.block.vital_block import VitalBlock
from vital_ai_vitalsigns.block.vital_block_file import VitalBlockFile
from vital_ai_vitalsigns.block.vital_block_reader import VitalBlockReader
from vital_ai_vitalsigns.block.vital_block_writer import VitalBlockWriter


URI_BASE = 'http://vital.ai/test/block/'


def build_objects():
    """A connected subgraph spanning three domain packages."""
    from ai_haley_kg_domain.model.KGEntity import KGEntity
    from com_vitalai_haley_taxonomy_domain.model.TaxonomyNode import \
        TaxonomyNode
    from com_vitalai_haley_taxonomy_domain.model.Edge_hasBroaderCategory \
        import Edge_hasBroaderCategory

    entity = KGEntity()
    entity.URI = URI_BASE + 'entity-1'
    entity.name = 'block entity'
    entity.kGEntityTypeDescription = 'block test entity'

    category = TaxonomyNode()
    category.URI = URI_BASE + 'category-1'
    category.name = 'block category'

    edge = Edge_hasBroaderCategory()
    edge.URI = URI_BASE + 'edge-1'
    edge.edgeSource = entity.URI
    edge.edgeDestination = category.URI

    return entity, edge, category


def test_block_roundtrip(vs, tmp_path):
    entity, edge, category = build_objects()

    path = str(tmp_path / 'domains.vital')

    writer = VitalBlockWriter(
        VitalBlockFile(path),
        encoding='jsonl',
        version='1.0.0',
        ontologies=[
            {'iri': 'http://vital.ai/ontology/haley-ai-kg',
             'version': '0.1.0'},
            {'iri': 'http://vital.ai/ontology/haley-taxonomy',
             'version': '0.1.0'},
        ],
        metadata={'description': 'domain test block file'},
    )
    writer.write_header()
    writer.write_block(VitalBlock([entity, edge, category]))
    writer.close()

    assert os.path.exists(path)

    reader = VitalBlockReader(VitalBlockFile(path))
    assert reader.get_encoding() == 'jsonl'

    blocks = list(reader)
    assert len(blocks) == 1

    objects = [blocks[0].first_object] + blocks[0].rest_objects
    assert len(objects) == 3

    by_uri = {str(o.URI): o for o in objects}

    restored_entity = by_uri[str(entity.URI)]
    assert type(restored_entity).__name__ == 'KGEntity'
    assert str(restored_entity.name) == 'block entity'
    assert str(restored_entity.kGEntityTypeDescription) == 'block test entity'

    restored_edge = by_uri[str(edge.URI)]
    assert type(restored_edge).__name__ == 'Edge_hasBroaderCategory'
    assert str(restored_edge.edgeSource) == str(entity.URI)
    assert str(restored_edge.edgeDestination) == str(category.URI)

    restored_category = by_uri[str(category.URI)]
    assert type(restored_category).__name__ == 'TaxonomyNode'


def test_block_multiple_blocks(vs, tmp_path):
    """Two blocks, read back in order with the same objects per block."""
    entity, edge, category = build_objects()

    path = str(tmp_path / 'multi.vital')

    writer = VitalBlockWriter(
        VitalBlockFile(path),
        encoding='jsonl',
        version='1.0.0',
        ontologies=[],
        metadata={},
    )
    writer.write_header()
    writer.write_block(VitalBlock([entity]))
    writer.write_block(VitalBlock([category, edge]))
    writer.close()

    blocks = list(VitalBlockReader(VitalBlockFile(path)))
    assert len(blocks) == 2
    assert str(blocks[0].first_object.URI) == str(entity.URI)
    assert len([blocks[1].first_object] + blocks[1].rest_objects) == 2
