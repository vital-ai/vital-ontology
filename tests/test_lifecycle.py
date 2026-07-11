"""Area 2: object lifecycle per domain (domain-testing-plan.md)."""

import pytest

from conftest import load_class, domain_node_params, domain_edge_params


URI_BASE = 'http://vital.ai/test/'


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_instantiate_and_core_properties(vs, domain, class_spec):
    """Instantiate each domain's node class; set/read URI and the inherited
    vital-core hasName property (cross-package inheritance)."""
    cls = load_class(class_spec)
    obj = cls()
    obj.URI = URI_BASE + cls.__name__ + '-1'
    obj.name = 'test-' + domain

    assert str(obj.URI) == URI_BASE + cls.__name__ + '-1'
    assert str(obj.name) == 'test-' + domain


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_class_uri_matches_ontology(vs, domain, class_spec):
    """get_class_uri() is a vital.ai ontology IRI containing the class name."""
    cls = load_class(class_spec)
    class_uri = cls.get_class_uri()
    assert class_uri.startswith('http://vital.ai/ontology/')
    assert class_uri.endswith('#' + cls.__name__)


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_undeclared_property_rejected(vs, domain, class_spec):
    """Setting a property not in allowed_properties raises."""
    cls = load_class(class_spec)
    obj = cls()
    obj.URI = URI_BASE + cls.__name__ + '-2'
    with pytest.raises(Exception):
        obj.definitelyNotARealProperty = 'nope'


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_domain_specific_property(vs, domain, class_spec):
    """Set/read one domain-declared (non-inherited) string property."""
    from vital_ai_vitalsigns.model.properties.StringProperty import \
        StringProperty
    cls = load_class(class_spec)
    own_string_props = [
        p['uri'] for p in cls._allowed_properties
        if p['prop_class'] is StringProperty
    ]
    if not own_string_props:
        pytest.skip(f'{cls.__name__} declares no own string property')
    obj = cls()
    obj.URI = URI_BASE + cls.__name__ + '-3'
    obj.set_property(own_string_props[0], 'domain-value')
    assert str(obj.get_property_value(own_string_props[0])) == 'domain-value'


@pytest.mark.parametrize('domain,class_spec', domain_edge_params())
def test_edge_source_destination(vs, domain, class_spec):
    """Edge classes carry source/destination URIs (vital-core properties)."""
    cls = load_class(class_spec)
    edge = cls()
    edge.URI = URI_BASE + cls.__name__ + '-1'
    edge.edgeSource = URI_BASE + 'src-1'
    edge.edgeDestination = URI_BASE + 'dst-1'
    assert str(edge.edgeSource) == URI_BASE + 'src-1'
    assert str(edge.edgeDestination) == URI_BASE + 'dst-1'


def test_cross_package_parent_chain(vs):
    """A chat-ai class inherits through aimp to vital-core: parent-declared
    properties are settable on the child (cross-package inheritance)."""
    from ai_chat_domain.model.AIMPMessageMetaInfo import AIMPMessageMetaInfo
    import com_vitalai_aimp_domain
    parents = [k.__module__.split('.')[0] for k in AIMPMessageMetaInfo.__mro__]
    assert 'com_vitalai_aimp_domain' in parents or \
        'vital_ai_vitalsigns' in parents
