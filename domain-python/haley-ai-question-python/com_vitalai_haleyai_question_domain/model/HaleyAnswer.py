
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


class HaleyAnswer(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAggregationRowURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAggregationType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAggregrationQuestionURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerDataType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerUnitType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyMappedAnswerType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPreferredSelectorType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isAggregationAnswer', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isCalculatedAnswerValue', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isDynamicRequiredAnswer', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isReadOnlyAnswerValue', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isSubjectToConstraints', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isSubjectToValidation', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyAnswer._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-question#HaleyAnswer'

