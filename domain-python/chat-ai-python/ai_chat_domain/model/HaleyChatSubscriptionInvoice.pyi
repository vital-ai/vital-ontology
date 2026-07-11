
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatSubscriptionInvoice(VITAL_Node):
        haleyChatStripeInvoiceId: str
        haleyChatSubscriptionPeriodEnd: datetime
        haleyChatSubscriptionPeriodStart: datetime

