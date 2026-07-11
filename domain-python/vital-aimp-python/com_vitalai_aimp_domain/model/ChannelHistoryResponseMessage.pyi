
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class ChannelHistoryResponseMessage(AIMPMessage):
        limit: int
        maxTimestamp: int
        messageSerialized: str
        messageURI: str
        messageURIs: str
        minTimestamp: int
        page: int
        recipient: str
        sender: str
        senderOrRecipient: str
        status: str
        totalPages: int

