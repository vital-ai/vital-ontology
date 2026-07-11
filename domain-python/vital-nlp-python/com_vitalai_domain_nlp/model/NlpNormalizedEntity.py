
from vital_ai_vitalsigns.model.properties.BooleanProperty import BooleanProperty
from vital_ai_vitalsigns.model.properties.DateTimeProperty import DateTimeProperty
from vital_ai_vitalsigns.model.properties.DoubleProperty import DoubleProperty
from vital_ai_vitalsigns.model.properties.FloatProperty import FloatProperty
from vital_ai_vitalsigns.model.properties.GeoLocationProperty import GeoLocationProperty
from vital_ai_vitalsigns.model.properties.IntegerProperty import IntegerProperty
from vital_ai_vitalsigns.model.properties.LongProperty import LongProperty
from vital_ai_vitalsigns.model.properties.OtherProperty import OtherProperty
from vital_ai_vitalsigns.model.properties.StringProperty import StringProperty
from vital_ai_vitalsigns.model.properties.TruthProperty import TruthProperty
from vital_ai_vitalsigns.model.properties.URIProperty import URIProperty
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class NlpNormalizedEntity(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasContext', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasEntityType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasHeightPx', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasImageDate', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasImageURL', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasNameVariants', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasNlpEntityCategory', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasShortname', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasSymbol', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasTicker', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasWidthPx', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasWikipediaURL', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasWordnetURI', 'prop_class': URIProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + NlpNormalizedEntity._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/vital-nlp#NlpNormalizedEntity'

