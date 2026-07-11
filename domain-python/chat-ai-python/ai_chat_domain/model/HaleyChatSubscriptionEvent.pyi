
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatSubscriptionEvent(VITAL_Node):
        haleyChatCustomerIdentifier: str
        haleyChatStripeInvoiceId: str
        haleyChatSubscriptionCreditAmount: int
        haleyChatSubscriptionEventStatusURI: str
        haleyChatSubscriptionEventTypeURI: str
        haleyChatSubscriptionEventUpdateDateTime: datetime
        haleyChatSubscriptionIdentifier: str
        haleyChatSubscriptionPeriodEnd: datetime
        haleyChatSubscriptionPeriodStart: datetime
        accountURI: str

