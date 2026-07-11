
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


class HaleyChatPayment(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPaymentAmount', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPaymentCurrencyURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPaymentDescription', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPaymentDueDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPaymentStatusCode', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPaymentStatusMessage', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPaymentStatusURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPaymentTimestamp', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasHaleyChatPaymentToken', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasReverseHaleyChatPaymentURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#isHaleyChatPaymentCurrent', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#isHaleyChatPaymentReverse', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyChatPayment._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/chat-ai#HaleyChatPayment'

