#!/usr/bin/env bash
# Generate the python code for one domain via the vitalsigns CLI, writing
# into build/generated/<domain>/ so committed code is never touched.
#
# Usage: tools/generate_domain.sh <domain> [output-base-dir]
#   e.g. tools/generate_domain.sh haley-taxonomy-python
#
# All generation logic lives in the vital-ai-vitalsigns package; this script
# only supplies this repository's paths.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

DOMAIN="${1:?usage: generate_domain.sh <domain> [output-base-dir]}"
OUTPUT_BASE="${2:-$REPO_ROOT/build/generated}"

vitalsigns generate \
    --domain "$DOMAIN" \
    --ontology-dir "$REPO_ROOT/vital-ontology" \
    --ontology-dir "$REPO_ROOT/domain-ontology" \
    --domain-config "$REPO_ROOT/domain-python/domain-config.yaml" \
    --output "$OUTPUT_BASE/$DOMAIN"
