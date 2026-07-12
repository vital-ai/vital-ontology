# Repository layout

```
vital-ontology/
├── vital-ontology/              Foundation OWL files
│   ├── vital-core-0.2.304.owl
│   └── vital-0.2.304.owl
├── domain-ontology/             Domain OWL files
│   ├── vital-nlp-0.2.304.owl
│   ├── vital-wordnet-0.2.304.owl
│   ├── vital-social-0.2.304.owl
│   ├── vital-aimp-0.1.0.owl
│   ├── haley-0.1.0.owl
│   ├── haley-taxonomy-0.1.0.owl
│   ├── haley-ai-question-0.1.0.owl
│   ├── haley-ai-kg-0.1.0.owl
│   ├── haley-ai-ml-0.1.0.owl
│   ├── chat-ai-0.1.0.owl
│   └── archive/                 Older OWL revisions
├── vital-domain-python/         The vital-ai-domain package
│   ├── pyproject.toml
│   ├── README.md
│   └── vital_ai_domain/        Generated code
├── domain-python/               The other 10 domain packages
│   ├── domain-config.yaml       Domain list for the generator
│   ├── chat-ai-python/
│   ├── haley-ai-kg-python/
│   ├── haley-ai-ml-python/
│   ├── haley-ai-question-python/
│   ├── haley-python/
│   ├── haley-taxonomy-python/
│   ├── vital-aimp-python/
│   ├── vital-nlp-python/
│   ├── vital-social-python/
│   └── vital-wordnet-python/
├── tools/                       Generation and build scripts
│   ├── generate_domain.sh       Wrapper calling vitalsigns CLI
│   ├── domain_order.py          Computes dependency order
│   ├── compare_generated.py     Diffs generated vs committed
│   ├── check_imports.py         Validates owl:imports closure
│   └── migrate_pyproject.py     setup.py → pyproject.toml tool
├── tests/                       Functionality test suite
│   ├── conftest.py              Domain matrix + VitalSigns fixture
│   ├── test_discovery.py
│   ├── test_lifecycle.py
│   ├── test_properties.py
│   ├── test_serialization.py
│   ├── test_block.py
│   ├── test_interop.py
│   └── fixtures/                Serialized objects from prior versions
├── vitalhome/                   Repo-local VITAL_HOME
│   └── conf/vitalsigns/         VitalSigns config for the CLI
├── docs/                        GitBook documentation (this site)
├── Makefile                     Build/test/publish automation
├── environment.yml              Conda environment definition
├── vital_env.env                VITAL_HOME pointer
└── .gitbook.yaml                GitBook root config
```

## Key directories

- **`vital-ontology/`** and **`domain-ontology/`** — the source OWL files.
  These are the source of truth; python code is generated from them.
- **`vital-domain-python/`** and **`domain-python/*/`** — the generated
  python packages. Each contains a `pyproject.toml`, `README.md`, and the
  generated package tree.
- **`tools/`** — helper scripts used by the Makefile. The generation
  pipeline invokes `tools/generate_domain.sh` per domain.
- **`tests/`** — pytest suite exercising all 11 packages against the
  published PyPI versions (156 tests).
- **`vitalhome/`** — a minimal VITAL_HOME directory so the `vitalsigns`
  CLI and tests can run without external configuration.
