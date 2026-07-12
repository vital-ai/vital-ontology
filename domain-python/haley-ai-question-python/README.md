# vital-ai-haley-question

Python bindings for the **haley-ai-question** ontology
(`http://vital.ai/ontology/haley-ai-question`, version 0.1.0) — question
and answer models: questions, typed answers (text, choice, date, number,
file, and more), answer constraints and dependencies, question sets, and
their connecting edges.

## Install

```bash
pip install vital-ai-haley-question
```

Direct dependency: `vital-ai-haley-taxonomy`.

## Usage

```python
from vital_ai_vitalsigns.vitalsigns import VitalSigns
from com_vitalai_haleyai_question_domain.model.HaleyQuestion import HaleyQuestion

vs = VitalSigns()

question = HaleyQuestion()
question.URI = 'http://example.org/question/1'
question.name = 'Example Question'

print(question.to_json())
```

## Notes

This package is generated from the OWL ontology — do not edit the code by
hand. Source ontology and generation pipeline:
[vital-ontology](https://github.com/vital-ai/vital-ontology).

## License

Apache License 2.0
