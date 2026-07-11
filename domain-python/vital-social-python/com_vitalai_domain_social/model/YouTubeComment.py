
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
from com_vitalai_domain_nlp.model.Document import Document


class YouTubeComment(Document):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/vital-social#hasAuthorName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasChannelID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasCommentID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasSocialLikeCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasVideoID', 'prop_class': StringProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + YouTubeComment._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/vital-social#YouTubeComment'

