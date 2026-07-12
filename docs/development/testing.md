# Testing

The repository has two complementary test mechanisms:

## 1. Parity checking (`make verify`)

Regenerates every domain and diffs the output against the committed
package tree. If there is any divergence the check fails. This ensures
the committed code is always exactly what the generator would produce.

```bash
make verify            # all domains
make verify-haley-ai-kg-python  # one domain
```

## 2. Functionality test suite (`make test`)

A pytest suite under `tests/` that exercises vitalsigns functionality
**through** the domain packages — confirming the generated code works
end-to-end, not just that it diffs cleanly.

```bash
make test
```

### Test areas (156 tests)

| Module | Area | What it tests |
|---|---|---|
| `test_discovery.py` | Package discovery | Entry points, registry build, class resolution |
| `test_lifecycle.py` | Object lifecycle | Instantiation, properties, rejection of undeclared props, edges, cross-package inheritance |
| `test_properties.py` | Property traits | Multi-value lists, new properties, datatypes, datetime |
| `test_serialization.py` | Serialization | JSON/RDF/dict/triples round-trips, cross-format stability |
| `test_block.py` | Block format | .vital block file write/read across domains |
| `test_interop.py` | Backward compat | Deserialize fixtures from prior package versions; version floors |

### How it works

- **`conftest.py`** defines a `DOMAINS` dict mapping every domain to a
  representative node class (and optionally an edge class). Tests are
  parametrized over this matrix.
- A session-scoped `VitalSigns()` fixture builds the registry once;
  subsequent tests run in <1s total.
- **`tests/fixtures/`** contains JSON files serialized by the previous
  PyPI versions (generated once with `generate_fixtures.py`), committed
  for regression testing.

### Running

```bash
# Full suite:
make test

# Verbose / single module:
python -m pytest tests/test_discovery.py -v

# CI ordering (recommended):
make verify && make test
```

### Adding a new domain

1. Add an entry to the `DOMAINS` dict in `tests/conftest.py`.
2. All parametrized tests automatically cover the new domain.
3. Optionally add a fixture file under `tests/fixtures/`.
