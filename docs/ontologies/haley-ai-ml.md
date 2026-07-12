# haley-ai-ml

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/haley-ai-ml` |
| **Version** | 0.1.0 |
| **OWL file** | `domain-ontology/haley-ai-ml-0.1.0.owl` |
| **Classes** | 43 |
| **Properties** | 92 |
| **Imports** | `haley` |
| **Python package** | [vital-ai-haley-ml](https://pypi.org/project/vital-ai-haley-ml/) |

## Purpose

Machine learning models: intents, features, predictions, recommendations,
and inference requests.

## Key classes

- **`HaleyIntent`** / **`HaleyIntentInstance`** — NLU intent definitions
  and detected instances.
- **`HaleyIntentSlotInstance`** — slot-filling for intents.
- **`FeatureGroup`** / **`FeatureType`** / **`FeatureValue`** — feature
  engineering representations.
- **`ActorMindRequest`** / **`AddContextMindRequest`** — inference
  interaction models.
- **Model selection edges** — `Edge_hasSelectedPredictionModel`,
  `Edge_hasSelectedRecommendationModel`, `Edge_hasSelectedPrompt`.
