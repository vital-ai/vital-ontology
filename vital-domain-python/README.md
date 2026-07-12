# vital-ai-domain

Python bindings for the **vital** ontology (`http://vital.ai/ontology/vital`,
version 0.2.304) — the general-purpose Vital AI domain layered directly on
`vital-core`. It defines widely shared application classes such as accounts,
logins, users, documents, files, events, places, organizations, jobs, and
datascripts, along with their connecting edges.

This package is the parent of all other Vital AI domain packages.

## Install

```bash
pip install vital-ai-domain
```

Depends on [vital-ai-vitalsigns](https://pypi.org/project/vital-ai-vitalsigns/),
which provides the `vital-core` bindings and runtime.

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from vital_ai_domain.model.Account import Account

vs = VitalSigns()  # discovers installed domain packages

account = Account()
account.URI = 'http://example.org/account/123'
account.name = 'Example Account'
account.accountID = 'acct-123'

print(account.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
