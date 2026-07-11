
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


class Tweet(Document):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/vital-social#hasAuthorID', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasAuthorName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasAuthorScreenName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasFavoriteCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasInReplyToScreenName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasInReplyToTweetID', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasInReplyToUserID', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasOriginalAuthorID', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasOriginalAuthorName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasOriginalAuthorScreenName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasRetweetCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasTweetID', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasTweetStatus', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasTwitterLatitude', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#hasTwitterLongitude', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-social#isRetweet', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + Tweet._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/vital-social#Tweet'

