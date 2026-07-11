
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatPendingPayment(VITAL_Node):
        haleyChatPaymentAmount: float
        haleyChatPaymentCurrencyURI: str
        haleyChatPaymentDescription: str
        haleyChatPaymentDueDateTime: datetime
        haleyChatPendingPaymentMessage: str
        haleyChatPendingPaymentTypeURI: str
        haleyChatStripeInvoiceId: str
        haleyChatSubscriptionInvoiceURI: str
        haleyChatSubscriptionURI: str

