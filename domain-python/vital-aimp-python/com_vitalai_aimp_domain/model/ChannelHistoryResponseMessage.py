
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
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class ChannelHistoryResponseMessage(AIMPMessage):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasLimit', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasMaxTimestamp', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasMessageSerialized', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasMessageURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasMessageURIs', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasMinTimestamp', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasPage', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasRecipient', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSender', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSenderOrRecipient', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasStatus', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasTotalPages', 'prop_class': IntegerProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + ChannelHistoryResponseMessage._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/vital-aimp#ChannelHistoryResponseMessage'

