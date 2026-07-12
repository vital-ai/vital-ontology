# Python packages overview

Each OWL ontology (except `vital-core`, which is bundled in vitalsigns)
has a corresponding python package published to PyPI. The packages
provide typed python classes generated from the OWL, used with the
[vital-ai-vitalsigns](https://pypi.org/project/vital-ai-vitalsigns/)
runtime.

## Package table

| PyPI package | Python import | Ontology |
|---|---|---|
| [vital-ai-domain](https://pypi.org/project/vital-ai-domain/) | `vital_ai_domain` | vital |
| [vital-ai-nlp](https://pypi.org/project/vital-ai-nlp/) | `com_vitalai_domain_nlp` | vital-nlp |
| [vital-ai-wordnet](https://pypi.org/project/vital-ai-wordnet/) | `com_vitalai_domain_wordnet` | vital-wordnet |
| [vital-ai-social](https://pypi.org/project/vital-ai-social/) | `com_vitalai_domain_social` | vital-social |
| [vital-ai-aimp](https://pypi.org/project/vital-ai-aimp/) | `com_vitalai_aimp_domain` | vital-aimp |
| [vital-ai-haley](https://pypi.org/project/vital-ai-haley/) | `com_vitalai_haley_domain` | haley |
| [vital-ai-haley-taxonomy](https://pypi.org/project/vital-ai-haley-taxonomy/) | `com_vitalai_haley_taxonomy_domain` | haley-taxonomy |
| [vital-ai-haley-question](https://pypi.org/project/vital-ai-haley-question/) | `com_vitalai_haleyai_question_domain` | haley-ai-question |
| [vital-ai-haley-kg](https://pypi.org/project/vital-ai-haley-kg/) | `ai_haley_kg_domain` | haley-ai-kg |
| [vital-ai-haley-ml](https://pypi.org/project/vital-ai-haley-ml/) | `ai_haley_ml_domain` | haley-ai-ml |
| [vital-ai-chat](https://pypi.org/project/vital-ai-chat/) | `ai_chat_domain` | chat-ai |

## Installation

Install any single package — pip resolves its full dependency chain:

```bash
# Install everything (leaf package pulls all parents):
pip install vital-ai-chat

# Or install just what you need:
pip install vital-ai-haley-kg
```

All packages require `vital-ai-vitalsigns>=0.1.54` and Python ≥ 3.10.

## Package discovery

VitalSigns discovers installed domain packages via the
`vitalsigns_packages` setuptools entry point. After installation,
initializing `VitalSigns()` automatically registers all classes and
properties from every installed package — no manual configuration needed.

## Versioning

Packages follow a cascading bump policy: when an upstream ontology
changes, all downstream packages also bump their versions and raise
their dependency floors. This ensures that installing any package always
pulls compatible versions of all its parents.
