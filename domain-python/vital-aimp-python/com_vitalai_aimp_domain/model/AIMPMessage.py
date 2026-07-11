
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


class AIMPMessage(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/vital#hasAccountURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital#hasLoginURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasActivityTaskIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasAuthSessionID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasBotURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChannelHistoryItem', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChannelHistoryListJSON', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChannelURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasChannelsHistory', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasDestinationAccountName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasDestinationAccountURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasDeviceInfo', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasEncryptedPayload', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasEndpointURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasGeoAPIJSON', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasGeolocation', 'prop_class': GeoLocationProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasIpAddress', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasJweEncryptedString', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasJweKeyIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasJwtEncodedString', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasJwtJSON', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasJwtKeyIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasKeyHash', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasLocalTime', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasMasterUserID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasPartialResultMessageCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasPartialResultPayloadCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasPartialResultTotalMessageCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasPartialResultTotalPayloadCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasPayload', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasPayloadStyleTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasQueueName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasReactionToSessionID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasRecipientIdentity', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasReplyChannelURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasRequestURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasRequestedPayloadStyleTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSenderIdentity', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSignature', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSourceAccountName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSourceAccountURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSourceRequestURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSourceUserID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSourceUserName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasText', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasTextToSpeak', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasThreadURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasTimezone', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasUserID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isAuthLoginTunnel', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isBroadcastOnly', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isCompressed', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isContainsPII', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isFinalResponse', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isHistoryMessage', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isInteractMode', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isInternalOnly', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isPartialResult', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isReplyTo', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isRequestCompression', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-core#hasSessionID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-core#hasUsername', 'prop_class': StringProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + AIMPMessage._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/vital-aimp#AIMPMessage'

