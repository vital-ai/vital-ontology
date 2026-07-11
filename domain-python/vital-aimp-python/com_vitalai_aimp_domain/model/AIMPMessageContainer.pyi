
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AIMPMessageContainer(VITAL_Node):
        accountURI: str
        loginURI: str
        aIMPMessageContainerTypeURI: str
        channelURI: str
        destinationAccountName: str
        destinationAccountURI: str
        recipientIdentity: str
        senderIdentity: str
        serializedMessage: str
        sourceAccountName: str
        sourceAccountURI: str
        sourceUserID: str
        sourceUserName: str
        replyTo: str

