"""Area 4: serialization round-trips per domain (domain-testing-plan.md)."""

import pytest

from vital_ai_vitalsigns.model.GraphObject import GraphObject

from conftest import load_class, domain_node_params, domain_edge_params


URI_BASE = 'http://vital.ai/test/'


def make_object(cls, suffix):
    obj = cls()
    obj.URI = URI_BASE + cls.__name__ + '-' + suffix
    obj.name = 'roundtrip-' + cls.__name__
    return obj


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_json_roundtrip(vs, domain, class_spec):
    """to_json -> GraphObject.from_json resolves the domain class via the
    registry and preserves values."""
    cls = load_class(class_spec)
    obj = make_object(cls, 'json')
    restored = GraphObject.from_json(obj.to_json())
    assert type(restored) is cls
    assert str(restored.URI) == str(obj.URI)
    assert str(restored.name) == str(obj.name)


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_json_compact_roundtrip(vs, domain, class_spec):
    cls = load_class(class_spec)
    obj = make_object(cls, 'jsonc')
    restored = GraphObject.from_json(obj.to_json(pretty_print=False))
    assert type(restored) is cls
    assert str(restored.name) == str(obj.name)


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_rdf_roundtrip(vs, domain, class_spec):
    """to_rdf (nt) -> GraphObject.from_rdf preserves class and values."""
    cls = load_class(class_spec)
    obj = make_object(cls, 'rdf')
    restored = GraphObject.from_rdf(obj.to_rdf())
    assert type(restored) is cls
    assert str(restored.URI) == str(obj.URI)
    assert str(restored.name) == str(obj.name)


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_dict_roundtrip(vs, domain, class_spec):
    cls = load_class(class_spec)
    obj = make_object(cls, 'dict')
    restored = GraphObject.from_dict(obj.to_dict())
    assert type(restored) is cls
    assert str(restored.URI) == str(obj.URI)
    assert str(restored.name) == str(obj.name)


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_triples_roundtrip(vs, domain, class_spec):
    cls = load_class(class_spec)
    obj = make_object(cls, 'triples')
    triples = obj.to_triples()
    assert len(triples) >= 2  # rdf:type + name at minimum


@pytest.mark.parametrize('domain,class_spec', domain_node_params())
def test_cross_format_stability(vs, domain, class_spec):
    """json -> object -> rdf -> object -> json is stable."""
    cls = load_class(class_spec)
    obj = make_object(cls, 'cross')
    via_json = GraphObject.from_json(obj.to_json())
    via_rdf = GraphObject.from_rdf(via_json.to_rdf())
    assert via_rdf.to_json() == obj.to_json()


@pytest.mark.parametrize('domain,class_spec', domain_edge_params())
def test_edge_roundtrip(vs, domain, class_spec):
    """Edge source/destination URIs survive a JSON round-trip."""
    cls = load_class(class_spec)
    edge = cls()
    edge.URI = URI_BASE + cls.__name__ + '-rt'
    edge.edgeSource = URI_BASE + 'src-rt'
    edge.edgeDestination = URI_BASE + 'dst-rt'
    restored = GraphObject.from_json(edge.to_json())
    assert type(restored) is cls
    assert str(restored.edgeSource) == URI_BASE + 'src-rt'
    assert str(restored.edgeDestination) == URI_BASE + 'dst-rt'


def test_multivalue_json_roundtrip(vs):
    """Multi-valued property survives a JSON round-trip."""
    from vital_ai_domain.model.Account import Account
    account = Account()
    account.URI = URI_BASE + 'account-mv'
    uris = [URI_BASE + 'a1', URI_BASE + 'a2']
    account.accountAccessURIs = uris
    restored = GraphObject.from_json(account.to_json())
    assert set(str(v) for v in restored.accountAccessURIs) == set(uris)
