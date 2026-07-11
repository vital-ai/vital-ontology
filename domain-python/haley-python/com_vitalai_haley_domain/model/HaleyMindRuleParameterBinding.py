
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


class HaleyMindRuleParameterBinding(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley#hasBinaryParameterBinding', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasBooleanParameterBinding', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasDateTimeParameterBinding', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasDoubleParameterBinding', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasIntegerParameterBinding', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasListBinaryParameterBinding', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasListBooleanParameterBinding', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasListDateTimeParameterBinding', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasListDoubleParameterBinding', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasListIntegerParameterBinding', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasListStringParameterBinding', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasListURIParameterBinding', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasParameterBindingVariable', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasStringParameterBinding', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasURIParameterBinding', 'prop_class': URIProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyMindRuleParameterBinding._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley#HaleyMindRuleParameterBinding'

