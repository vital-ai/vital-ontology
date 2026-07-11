from vital_ai_vitalsigns.model.trait.PropertyTrait import PropertyTrait


class Property_isMultivalueProperty(PropertyTrait):
    namespace = "http://vital.ai/ontology/vital-aimp#"
    local_name = "isMultivalueProperty"
    multiple_values = False
