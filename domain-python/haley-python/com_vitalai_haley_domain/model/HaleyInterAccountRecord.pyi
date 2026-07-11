
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyInterAccountRecord(VITAL_Node):
        interAccountDestinationChannelURI: str
        interAccountRecipientAccountURI: str
        interAccountRecipientLoginURI: str
        interAccountReplyMessageURI: str
        interAccountRequestDateTime: datetime
        interAccountRequestURI: str
        interAccountResponseDateTime: datetime
        interAccountResponseStatusURI: str
        interAccountResponseURI: str
        interAccountSenderAccountURI: str
        interAccountSenderLoginURI: str
        interAccountSenderMessageURI: str
        interAccountSerializedRequest: str
        interAccountSerializedResponse: str
        interAccountSourceChannelURI: str

