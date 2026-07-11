
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


class HaleyChatAccountInfo(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatAccountCategoryURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatAccountEntityName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatAccountOwnerLoginURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatAccountUseCaseURIs', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatCustomerIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatOnboardingInteractionURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatOnboardingStatusURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPaymentProcessorURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPrimaryCountryURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPrimaryCurrencyURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPrimaryLanguageURI', 'prop_class': URIProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyChatAccountInfo._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/chat-ai#HaleyChatAccountInfo'

