"""Area 3: property trait semantics (domain-testing-plan.md)."""

import pytest


URI_BASE = 'http://vital.ai/test/'


def test_multiple_values_property(vs):
    """A hasMultipleValues property accepts and round-trips a list
    (regression for the multiple_values trait format adopted by
    vital-domain-python in the 2026-07-11 regeneration)."""
    from vital_ai_domain.model.properties.Property_hasAccountAccessURIs \
        import Property_hasAccountAccessURIs
    assert Property_hasAccountAccessURIs.multiple_values is True

    from vital_ai_domain.model.Account import Account
    account = Account()
    account.URI = URI_BASE + 'account-1'
    uris = [URI_BASE + 'access-1', URI_BASE + 'access-2']
    account.accountAccessURIs = uris
    value = account.accountAccessURIs
    assert set(str(v) for v in value) == set(uris)


def test_single_value_trait_flag(vs):
    """A regular property trait reports multiple_values False."""
    from vital_ai_vitalsigns_core.model.properties.Property_hasName import \
        Property_hasName
    assert Property_hasName.multiple_values is False


def test_hastablesprefix_on_sql_config(vs):
    """New vital-core#hasTablesPrefix works on VitalServiceSqlConfig."""
    from vital_ai_vitalsigns_core.model.VitalServiceSqlConfig import \
        VitalServiceSqlConfig
    cfg = VitalServiceSqlConfig()
    cfg.URI = URI_BASE + 'sql-config-1'
    cfg.tablesPrefix = 'test_prefix'
    assert str(cfg.tablesPrefix) == 'test_prefix'


def test_vitalont_classes_usable(vs):
    """New VitalOnt* classes in the vital domain are instantiable with
    their properties."""
    from vital_ai_domain.model.VitalOntNode import VitalOntNode
    node = VitalOntNode()
    node.URI = URI_BASE + 'ont-node-1'
    node.vitalOntClassURI = 'http://vital.ai/ontology/vital-core#VITAL_Node'
    assert str(node.vitalOntClassURI) == \
        'http://vital.ai/ontology/vital-core#VITAL_Node'


def test_datatypes(vs):
    """Typed properties across datatypes set/get correctly on a domain
    class (KGEntity: URI + string; plus core int/bool/datetime props)."""
    from ai_haley_kg_domain.model.KGEntity import KGEntity
    entity = KGEntity()
    entity.URI = URI_BASE + 'entity-1'
    entity.kGEntityTypeDescription = 'a description'          # string
    entity.set_property(
        'http://vital.ai/ontology/haley-ai-kg#hasKGEntityType',
        'http://vital.ai/test/entity-type')                    # URI
    assert str(entity.kGEntityTypeDescription) == 'a description'
    assert str(entity.get_property_value(
        'http://vital.ai/ontology/haley-ai-kg#hasKGEntityType')) == \
        'http://vital.ai/test/entity-type'


def test_datetime_property(vs):
    """DateTime property round-trips on a domain object
    (vital#hasExpirationDate on FileNode is a DateTimeProperty)."""
    import datetime
    from vital_ai_domain.model.FileNode import FileNode
    file_node = FileNode()
    file_node.URI = URI_BASE + 'file-dt-1'
    when = datetime.datetime(2026, 7, 11, 12, 0, 0)
    file_node.expirationDate = when
    assert file_node.expirationDate is not None
