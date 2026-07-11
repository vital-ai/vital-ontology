
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
from ai_chat_domain.model.HaleyChatMessage import HaleyChatMessage


class HaleyChatBotMessage(HaleyChatMessage):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/chat-ai#hasAgentInstallURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasAgentVariantURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasChatGeneratedMessage', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasChatIncrementalGeneratedMessage', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasChatPartialGeneratedMessage', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasChatPriorUserMessage', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasChatVoiceMessage', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatQuotaStatusURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatReplyToIntentURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#isChatContinueListening', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyChatBotMessage._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/chat-ai#HaleyChatBotMessage'

