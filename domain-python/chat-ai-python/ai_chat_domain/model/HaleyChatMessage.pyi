
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatMessage(VITAL_Node):
        bridgeHaleyMessageURI: str
        chatEncodedVoiceContentType: str
        chatEncodedVoiceData: str
        chatEndTimestamp: datetime
        chatIncrementalEncodedVoiceData: str
        chatIncrementalTextMessage: str
        chatMessageActorSequence: str
        chatMessageIPAddress: str
        chatMessageSequence: int
        chatPartialEncodedVoiceData: str
        chatPartialTextMessage: str
        chatStartTimestamp: datetime
        chatTextMessage: str
        chatTimestamp: datetime
        chatVoicePath: str
        haleyChatCreditSourceURI: str
        haleyChatInteractionModeURI: str
        haleyChatInteractionModelProviderURI: str
        haleyChatInteractionResponseModeURI: str
        haleyChatInteractionURI: str
        haleyChatMessageCreditUsed: int
        haleyChatMessageType: str
        haleyChatTextToSpeak: str
        haleyChatVoiceLanguageTypeURI: str
        messageRequestURI: str
        chatIncrementalMessage: bool
        chatPartialMessage: bool
        accountURI: str
        loginURI: str
        channelURI: str
        geoAPIJSON: str
        sessionID: str

