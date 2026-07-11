
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class GetChannelHistoryMessage(AIMPMessage):
        limit: int
        maxTimestamp: int
        messageURI: str
        messageURIs: str
        minTimestamp: int
        recipient: str
        sender: str
        senderOrRecipient: str

