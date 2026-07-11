
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


class AIMPTask(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasAIMPMessageContentURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasAIMPTaskProgressURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasAIMPTaskStatusURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasAIMPTaskTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChatCompletionTokenCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChatPromptTokenCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChatTaskDeltaTime', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChatTaskEndDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChatTaskStagesJSON', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChatTaskStartDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChatTaskUpdateDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChatTotalTokenCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasMessageURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasTimezone', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isDaylightSavingsTime', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + AIMPTask._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/vital-aimp#AIMPTask'

