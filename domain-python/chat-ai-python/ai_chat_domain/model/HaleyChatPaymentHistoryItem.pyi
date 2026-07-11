
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatPaymentHistoryItem(VITAL_Node):
        haleyChatPaymentAmount: float
        haleyChatPaymentCurrencyURI: str
        haleyChatPaymentDescription: str
        haleyChatPaymentDueDateTime: datetime
        haleyChatPaymentStatusCode: str
        haleyChatPaymentStatusMessage: str
        haleyChatPaymentStatusURI: str
        haleyChatPaymentTimestamp: datetime
        haleyChatPaymentReverse: bool

