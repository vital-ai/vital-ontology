
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatAgentThought(VITAL_Node):
        bridgeHaleyMessageURI: str
        haleyChatAgentThoughtTypeURI: str
        haleyChatInteractionURI: str
        haleyChatMessageHistoryURI: str
        haleyChatMessageURI: str
        haleyChatReferenceMessageURI: str
        haleyChatThoughtSequence: int
        haleyChatThoughtText: str
        haleyChatThoughtTitle: str
        chatIncrementalMessage: bool
        chatPartialMessage: bool
        haleyChatThoughtComplete: bool
        aIMPMessageContentURI: str

