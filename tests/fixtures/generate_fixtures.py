"""One-time fixture generator for test_interop.py.

Run with the PREVIOUS domain package versions installed (see
planning/domain-testing-plan.md area 6), from the repo root:

    build/fixture-venv/bin/python tests/fixtures/generate_fixtures.py

The committed fixtures capture the wire format produced by apps using the
pre-regeneration packages (vital-ai-domain 0.1.7, vital-ai-haley-kg 0.1.24,
vital-ai-chat 0.1.20).
"""

import os
import sys

FIXTURES_DIR = os.path.dirname(os.path.abspath(__file__))

URI_BASE = 'http://vital.ai/test/interop/'


def main():
    from vital_ai_vitalsigns.vitalsigns import VitalSigns
    VitalSigns()

    from importlib.metadata import version

    from vital_ai_domain.model.Account import Account
    from ai_haley_kg_domain.model.KGEntity import KGEntity
    from ai_chat_domain.model.AIMPMessageMetaInfo import AIMPMessageMetaInfo

    versions = {
        'vital-ai-domain': version('vital-ai-domain'),
        'vital-ai-haley-kg': version('vital-ai-haley-kg'),
        'vital-ai-chat': version('vital-ai-chat'),
        'vital-ai-vitalsigns': version('vital-ai-vitalsigns'),
    }
    print(f"generating fixtures with: {versions}")

    account = Account()
    account.URI = URI_BASE + 'account-1'
    account.name = 'interop account'
    account.accountID = 'interop-account-id'

    entity = KGEntity()
    entity.URI = URI_BASE + 'entity-1'
    entity.name = 'interop entity'
    entity.kGEntityTypeDescription = 'interop test entity'

    meta = AIMPMessageMetaInfo()
    meta.URI = URI_BASE + 'meta-1'
    meta.name = 'interop meta'

    for filename, obj in [
        ('account.json', account),
        ('kgentity.json', entity),
        ('aimpmessagemetainfo.json', meta),
    ]:
        path = os.path.join(FIXTURES_DIR, filename)
        with open(path, 'w') as f:
            f.write(obj.to_json())
        print(f"wrote {path}")

    with open(os.path.join(FIXTURES_DIR, 'VERSIONS.txt'), 'w') as f:
        for k, v in sorted(versions.items()):
            f.write(f"{k}=={v}\n")


if __name__ == '__main__':
    sys.exit(main())
