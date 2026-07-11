
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGChatMessage(KGNode):
        kGChatInteractionURI: str
        kGChatMessageDateTime: datetime
        kGChatMessageSequence: int
        kGChatMessageText: str
        kGChatMessageType: str
        kGRoomURI: str
        primaryLanguageType: str

