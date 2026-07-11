
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


class KGUserContext(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGPlaceURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextAccountLevel', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextAccountURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextAgentFamiliarity', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextAgentTone', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextCurrentDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextCurrentTimezone', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextExperienceLevel', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextGender', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextLightLevel', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextLocation', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextLoginURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextMood', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextPronoun', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGUserContextSoundLevel', 'prop_class': DoubleProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + KGUserContext._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-kg#KGUserContext'

