
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


class HaleyQuestion(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyGroupDisplayTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyLanguageType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyQuestionStatus', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHorizontalColumnAssignment', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasQuestionAbbreviatedText', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasQuestionFriendlyText', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasQuestionGroupIndex', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasQuestionIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasQuestionProfessionalText', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasQuestionText', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isDependencyEnabled', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isHiddenInGroupDisplay', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isHiddenInPopform', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isHiddenQuestion', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isIncludeInSectionPopform', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isNotificationContent', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isRowNameQuestion', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasDescription', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasLongDescription', 'prop_class': StringProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyQuestion._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-question#HaleyQuestion'

