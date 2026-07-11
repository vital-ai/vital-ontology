
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


class KGEMail(KGNode):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEMailType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEmailBCCAddressList', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEmailCCAddressList', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEmailRecipientAddress', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEmailRecipientName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEmailSendDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEmailSenderAddress', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEmailSenderName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEmailSubject', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEmailSummary', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGEmailToAddressList', 'prop_class': StringProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + KGEMail._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-kg#KGEMail'

