"""Area 6: interop / regression against previous versions
(domain-testing-plan.md).

Fixtures under tests/fixtures/ were serialized once by the PREVIOUS domain
package versions (see fixtures/VERSIONS.txt, generate_fixtures.py) and must
keep deserializing with the current packages.
"""

import os
from importlib.metadata import version

import pytest

from vital_ai_vitalsigns.model.GraphObject import GraphObject


FIXTURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'fixtures')

URI_BASE = 'http://vital.ai/test/interop/'


def load_fixture(filename):
    with open(os.path.join(FIXTURES_DIR, filename)) as f:
        return f.read()


def test_account_fixture(vs):
    """JSON written by vital-ai-domain 0.1.7 loads with the current package."""
    from vital_ai_domain.model.Account import Account
    obj = GraphObject.from_json(load_fixture('account.json'))
    assert type(obj) is Account
    assert str(obj.URI) == URI_BASE + 'account-1'
    assert str(obj.name) == 'interop account'
    assert str(obj.accountID) == 'interop-account-id'


def test_kgentity_fixture(vs):
    """JSON written by vital-ai-haley-kg 0.1.24 loads with the current
    package."""
    from ai_haley_kg_domain.model.KGEntity import KGEntity
    obj = GraphObject.from_json(load_fixture('kgentity.json'))
    assert type(obj) is KGEntity
    assert str(obj.URI) == URI_BASE + 'entity-1'
    assert str(obj.kGEntityTypeDescription) == 'interop test entity'


def test_aimpmessagemetainfo_fixture(vs):
    """JSON written by vital-ai-chat 0.1.20 loads with the current package."""
    from ai_chat_domain.model.AIMPMessageMetaInfo import AIMPMessageMetaInfo
    obj = GraphObject.from_json(load_fixture('aimpmessagemetainfo.json'))
    assert type(obj) is AIMPMessageMetaInfo
    assert str(obj.URI) == URI_BASE + 'meta-1'
    assert str(obj.name) == 'interop meta'


def test_fixture_reserialization_stable(vs):
    """Old-format fixtures reserialize with the current packages without
    losing properties."""
    for filename in ('account.json', 'kgentity.json',
                     'aimpmessagemetainfo.json'):
        obj = GraphObject.from_json(load_fixture(filename))
        rt = GraphObject.from_json(obj.to_json())
        assert type(rt) is type(obj)
        assert str(rt.URI) == str(obj.URI)


MINIMUM_VERSIONS = {
    'vital-ai-domain': '0.1.9',
    'vital-ai-nlp': '0.1.6',
    'vital-ai-wordnet': '0.1.6',
    'vital-ai-social': '0.1.6',
    'vital-ai-aimp': '0.1.17',
    'vital-ai-haley': '0.1.9',
    'vital-ai-haley-taxonomy': '0.1.7',
    'vital-ai-haley-question': '0.1.7',
    'vital-ai-haley-kg': '0.1.25',
    'vital-ai-haley-ml': '0.1.7',
    'vital-ai-chat': '0.1.21',
    'vital-ai-vitalsigns': '0.1.54',
}


@pytest.mark.parametrize('package,minimum', sorted(MINIMUM_VERSIONS.items()))
def test_installed_versions(package, minimum):
    """The environment runs at least the 2026-07-11 published versions."""
    from packaging.version import Version
    assert Version(version(package)) >= Version(minimum)
