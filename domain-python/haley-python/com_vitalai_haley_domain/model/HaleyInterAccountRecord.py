
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


class HaleyInterAccountRecord(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountDestinationChannelURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountRecipientAccountURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountRecipientLoginURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountReplyMessageURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountRequestDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountRequestURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountResponseDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountResponseStatusURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountResponseURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountSenderAccountURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountSenderLoginURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountSenderMessageURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountSerializedRequest', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountSerializedResponse', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasInterAccountSourceChannelURI', 'prop_class': URIProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyInterAccountRecord._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley#HaleyInterAccountRecord'

