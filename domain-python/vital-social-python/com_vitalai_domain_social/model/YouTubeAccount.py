
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
from com_vitalai_domain_social.model.SocialMediaAccount import SocialMediaAccount


class YouTubeAccount(SocialMediaAccount):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/vital-social#hasChannelID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasCommentCount', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasCountry', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasExpiresIn', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasPublishedAt', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasRefreshToken', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasSocialDescription', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasSubscriberCount', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasVideoCount', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasViewCount', 'prop_class': LongProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + YouTubeAccount._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/vital-social#YouTubeAccount'

