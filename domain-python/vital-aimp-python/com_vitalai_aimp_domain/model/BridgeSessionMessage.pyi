
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class BridgeSessionMessage(AIMPMessage):
        bridgeAccountURI: str
        bridgeChannelURI: str
        bridgeSequenceNumber: int
        bridgeSessionID: str
        replyBridgeReferenceObjectURI: str
        serializedBridgeMessage: str

