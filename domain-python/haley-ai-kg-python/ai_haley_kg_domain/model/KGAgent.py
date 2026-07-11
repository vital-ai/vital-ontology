
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
from ai_haley_kg_domain.model.KGNode import KGNode


class KGAgent(KGNode):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentAvatarImageSourceURL', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentAvatarImageURL', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentAvatarLargeImageURL', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentDeploymentURL', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentDescription', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentImplIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentModificationDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentNameSlug', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentPublishStatusURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentPublisherName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentRankingScore', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentRankingScoreUpdateDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentServiceURIs', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGAgentType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGBracketURIs', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasPrimaryLanguageType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasTopCategoryURIs', 'prop_class': URIProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + KGAgent._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-kg#KGAgent'

