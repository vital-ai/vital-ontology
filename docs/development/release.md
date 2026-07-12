# Release process

## When to release

A new release is needed when:

- An OWL ontology changes (new/modified classes or properties).
- The vitalsigns runtime changes in a way that affects generated code
  (e.g. new property trait semantics).
- A downstream application needs a bug fix or addition.

## Versioning policy: cascading bumps

When a package changes, **every downstream package also bumps**:

- The changed package increments its version.
- Each downstream package increments its version AND raises its
  `dependencies` floor in `pyproject.toml` to require the new parent.

This ensures that `pip install <any-leaf-package>` always pulls a
consistent, tested set of versions for the whole chain.

Example: a change to the `vital` ontology (vital-ai-domain) triggers
bumps to all 10 downstream packages; a change to haley-ai-kg bumps
haley-ai-kg, haley-ai-ml (if it depends), and chat-ai.

## Step-by-step release

1. **Edit the OWL** — make your changes in `vital-ontology/` or
   `domain-ontology/`; bump `owl:versionInfo`.

2. **Regenerate** — `make generate`; review with `make verify-<domain>`.

3. **Adopt** — copy the generated output into the committed package
   tree (replace the old `model/` directory).

4. **Bump versions** — edit `pyproject.toml` for the changed package
   and all its dependents: increment `version`, raise `dependencies`
   floors.

5. **Build and test**:
   ```bash
   make build
   make test-install
   make test
   ```

6. **Publish**:
   ```bash
   make publish
   ```
   This uploads all packages in dependency order with `--skip-existing`
   so only bumped packages are actually uploaded.

## Where versions live

- **Package version**: `pyproject.toml` → `[project] version`
- **OWL version**: `owl:versionInfo` in the OWL file
- **Dependency floors**: `pyproject.toml` → `[project] dependencies`

## Notes

- `make publish` uses `twine upload` with `--skip-existing` — safe to
  run multiple times.
- The Makefile processes packages in dependency order (from
  `tools/domain_order.py`) so that parent packages are available on
  PyPI before children are uploaded.
- There is no separate "release branch" workflow — releases happen from
  `main`.
