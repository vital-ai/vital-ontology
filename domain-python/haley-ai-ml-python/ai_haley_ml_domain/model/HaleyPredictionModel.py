
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


class HaleyPredictionModel(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-ml#hasModelIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-ml#hasPredictionImplementingClass', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-ml#hasPredictionModelClassURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-ml#hasPredictionModelEndpoint', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-ml#hasPredictionModelProvider', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-ml#hasPredictionModelStructureType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-ml#hasPredictionModelType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-ml#hasVersion', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-ml#isGlobalPredictionModel', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyPredictionModel._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-ml#HaleyPredictionModel'

