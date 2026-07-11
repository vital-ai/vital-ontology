
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
from vital_ai_vitalsigns_core.model.VITAL_PeerEdge import VITAL_PeerEdge


class Edge_hasQuestion(VITAL_PeerEdge):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerConstraintScopeType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerValidationScopeType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPageNumber', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasQuestionIndex', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasRank', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isDynamicRequiredQuestion', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isHighlighted', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isRequiredQuestion', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#isSuppressedQuestion', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + Edge_hasQuestion._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-question#Edge_hasQuestion'

