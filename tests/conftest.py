"""Shared fixtures and the domain matrix for the domain-package tests
(planning/domain-testing-plan.md).

Requires the published packages installed (vital-ai-vitalsigns>=0.1.54 and
the 11 domain packages). VITAL_HOME is resolved by vitalsigns via the
repo's vital_env.env when pytest runs from the repo root.
"""

import pytest


# One entry per domain package: entry-point module name and a representative
# node class (module path within the package + class name). Edge classes for
# edge round-trip tests where noted.
DOMAINS = {
    'vital-domain-python': {
        'module': 'vital_ai_domain',
        'node_class': ('vital_ai_domain.model.Account', 'Account'),
    },
    'vital-nlp-python': {
        'module': 'com_vitalai_domain_nlp',
        'node_class': ('com_vitalai_domain_nlp.model.Document', 'Document'),
    },
    'vital-wordnet-python': {
        'module': 'com_vitalai_domain_wordnet',
        'node_class': ('com_vitalai_domain_wordnet.model.SynsetNode',
                       'SynsetNode'),
        'edge_class': ('com_vitalai_domain_wordnet.model.Edge_WordnetAntonym',
                       'Edge_WordnetAntonym'),
    },
    'vital-social-python': {
        'module': 'com_vitalai_domain_social',
        'node_class': ('com_vitalai_domain_social.model.DirectMessage',
                       'DirectMessage'),
    },
    'vital-aimp-python': {
        'module': 'com_vitalai_aimp_domain',
        'node_class': ('com_vitalai_aimp_domain.model.AIMPMessage',
                       'AIMPMessage'),
    },
    'haley-python': {
        'module': 'com_vitalai_haley_domain',
        'node_class': ('com_vitalai_haley_domain.model.CloudBucket',
                       'CloudBucket'),
    },
    'haley-taxonomy-python': {
        'module': 'com_vitalai_haley_taxonomy_domain',
        'node_class': (
            'com_vitalai_haley_taxonomy_domain.model.TaxonomyNode',
            'TaxonomyNode'),
        'edge_class': (
            'com_vitalai_haley_taxonomy_domain.model.Edge_hasBroaderCategory',
            'Edge_hasBroaderCategory'),
    },
    'haley-ai-question-python': {
        'module': 'com_vitalai_haleyai_question_domain',
        'node_class': (
            'com_vitalai_haleyai_question_domain.model.HaleyQuestion',
            'HaleyQuestion'),
    },
    'haley-ai-kg-python': {
        'module': 'ai_haley_kg_domain',
        'node_class': ('ai_haley_kg_domain.model.KGEntity', 'KGEntity'),
    },
    'haley-ai-ml-python': {
        'module': 'ai_haley_ml_domain',
        'node_class': ('ai_haley_ml_domain.model.HaleyIntent',
                       'HaleyIntent'),
    },
    'chat-ai-python': {
        'module': 'ai_chat_domain',
        'node_class': ('ai_chat_domain.model.AIMPMessageMetaInfo',
                       'AIMPMessageMetaInfo'),
    },
}


def load_class(spec):
    """Import ('module.path', 'ClassName') -> class object."""
    import importlib
    module_path, class_name = spec
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


@pytest.fixture(scope='session')
def vs():
    """Session-scoped VitalSigns singleton (registry built on first init)."""
    from vital_ai_vitalsigns.vitalsigns import VitalSigns
    return VitalSigns()


@pytest.fixture(scope='session')
def registry(vs):
    return vs.get_registry()


def domain_node_params():
    """(domain, node class spec) params for parametrized tests."""
    return [
        pytest.param(name, cfg['node_class'], id=name)
        for name, cfg in DOMAINS.items()
    ]


def domain_edge_params():
    return [
        pytest.param(name, cfg['edge_class'], id=name)
        for name, cfg in DOMAINS.items() if 'edge_class' in cfg
    ]
