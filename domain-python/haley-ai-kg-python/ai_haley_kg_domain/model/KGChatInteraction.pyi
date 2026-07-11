
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGChatInteraction(KGNode):
        kGChannelURI: str
        kGChatInteractionCompleteText: str
        kGChatInteractionSummaryText: str
        kGChatInteractionType: str
        kGRoomURI: str

