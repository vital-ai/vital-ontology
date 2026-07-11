"""Area 1: package discovery & registry (domain-testing-plan.md)."""

from importlib.metadata import entry_points

import pytest

from conftest import DOMAINS, load_class, domain_node_params


EXPECTED_ENTRY_POINTS = {cfg['module'] for cfg in DOMAINS.values()} | {
    'vital_ai_vitalsigns',
    'vital_ai_vitalsigns_core',
}


def test_entry_points_present():
    """All 11 domain packages + vitalsigns core register the
    vitalsigns_packages entry point."""
    found = {ep.name for ep in entry_points(group='vitalsigns_packages')}
    missing = EXPECTED_ENTRY_POINTS - found
    assert not missing, f"missing vitalsigns_packages entry points: {missing}"


def test_vitalsigns_initializes(vs):
    """VitalSigns() init (which builds the registry) succeeds with all
    domain packages installed."""
    assert vs is not None
    assert vs.get_registry() is not None


def test_registry_has_classes(registry):
    """Registry contains a non-trivial number of classes and property
    traits after scanning all packages."""
    assert len(registry.vitalsigns_classes) > 1000
    assert len(registry.vitalsigns_property_classes) > 1000


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_registry_resolves_domain_class(registry, domain, class_spec):
    """A class URI from every domain resolves to the right python class."""
    cls = load_class(class_spec)
    resolved = registry.get_vitalsigns_class(cls.get_class_uri())
    assert resolved is cls


def test_new_vitalont_class_registered(registry):
    """The VitalOnt* additions to the vital ontology are registered."""
    from vital_ai_domain.model.VitalOntNode import VitalOntNode
    resolved = registry.get_vitalsigns_class(VitalOntNode.get_class_uri())
    assert resolved is VitalOntNode


def test_new_hastablesprefix_property_registered(registry):
    """vital-core#hasTablesPrefix (added 2026-07-11) has a property trait."""
    prop_cls = registry.get_vitalsigns_property_class(
        'http://vital.ai/ontology/vital-core#hasTablesPrefix')
    assert prop_cls.get_uri() == \
        'http://vital.ai/ontology/vital-core#hasTablesPrefix'
