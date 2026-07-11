# Build all domain python packages from the OWL sources, in dependency order.
#
# Requires the conda env from environment.yml (python 3.12 + vital-ai-vitalsigns):
#   conda env create -f environment.yml && conda activate vital-ontology
#
# Build order is computed from owl:imports by tools/domain_order.py (which
# uses the vitalsigns library); generation itself runs only the vitalsigns CLI
# (tools/generate_domain.sh).

PYTHON ?= python
OUTPUT_BASE ?= build/generated
TEST_VENV ?= build/test-venv

DOMAINS := $(shell $(PYTHON) tools/domain_order.py)

# package dir for a domain: vital-domain-python lives at the repo root,
# all other domains under domain-python/
pkgdir = $(if $(filter vital-domain-python,$(1)),vital-domain-python,domain-python/$(1))

.PHONY: help deps order check-imports generate verify test build test-install publish clean \
	$(addprefix generate-,$(DOMAINS)) $(addprefix verify-,$(DOMAINS)) \
	$(addprefix build-,$(DOMAINS)) $(addprefix publish-,$(DOMAINS))

help:
	@echo "Targets:"
	@echo "  order              print domains in dependency (build) order"
	@echo "  check-imports      verify the owl:imports closure is complete"
	@echo "  generate           generate all domains in dependency order"
	@echo "  generate-<domain>  generate one domain (e.g. generate-haley-python)"
	@echo "  verify             generate + compare all domains against committed code"
	@echo "  verify-<domain>    generate + compare one domain"
	@echo "  test               run the domain functionality test suite (tests/)"
	@echo "  deps               install build/publish tools (build, twine)"
	@echo "  build              build sdist+wheel for all domains in dependency order"
	@echo "  build-<domain>     build one domain package"
	@echo "  test-install       install built wheels into a fresh venv + smoke-test imports"
	@echo "  publish            twine upload all domains in dependency order (--skip-existing)"
	@echo "  publish-<domain>   twine upload one domain"
	@echo "  clean              remove $(OUTPUT_BASE), $(TEST_VENV) and package dist dirs"

order:
	@$(PYTHON) tools/domain_order.py --verbose

check-imports:
	$(PYTHON) tools/check_imports.py

generate: $(addprefix generate-,$(DOMAINS))

$(addprefix generate-,$(DOMAINS)): generate-%:
	@echo "=== generating $*"
	@tools/generate_domain.sh $* $(OUTPUT_BASE) > /dev/null

verify: $(addprefix verify-,$(DOMAINS))

$(addprefix verify-,$(DOMAINS)): verify-%: generate-%
	@$(PYTHON) tools/compare_generated.py $* --generated-base $(OUTPUT_BASE)

test:
	$(PYTHON) -m pytest tests/ -q

deps:
	$(PYTHON) -m pip install --upgrade build twine

build: $(addprefix build-,$(DOMAINS))

$(addprefix build-,$(DOMAINS)): build-%:
	@echo "=== building $*"
	cd $(call pkgdir,$*) && rm -rf build dist *.egg-info && $(PYTHON) -m build > /dev/null
	@ls $(call pkgdir,$*)/dist

test-install: build
	rm -rf $(TEST_VENV)
	$(PYTHON) -m venv $(TEST_VENV)
	$(TEST_VENV)/bin/pip install --quiet --upgrade pip
	for d in $(DOMAINS); do \
		case $$d in vital-domain-python) p=vital-domain-python ;; *) p=domain-python/$$d ;; esac; \
		echo "=== installing $$d"; \
		$(TEST_VENV)/bin/pip install --quiet $$p/dist/*.whl || exit 1; \
	done
	for d in $(DOMAINS); do \
		case $$d in vital-domain-python) p=vital-domain-python ;; *) p=domain-python/$$d ;; esac; \
		pkg=$$(basename $$(dirname $$(find $$p -maxdepth 2 -name '__init__.py' | head -1))); \
		echo "=== importing $$pkg"; \
		$(TEST_VENV)/bin/python -c "import $$pkg" || exit 1; \
	done
	@echo "test-install OK"

publish: $(addprefix publish-,$(DOMAINS))

$(addprefix publish-,$(DOMAINS)): publish-%:
	@echo "=== publishing $*"
	$(PYTHON) -m twine upload --skip-existing $(call pkgdir,$*)/dist/*

clean:
	rm -rf $(OUTPUT_BASE) $(TEST_VENV)
	for d in $(DOMAINS); do \
		case $$d in vital-domain-python) p=vital-domain-python ;; *) p=domain-python/$$d ;; esac; \
		rm -rf $$p/build $$p/dist $$p/*.egg-info; \
	done
