
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatCreditEvent(VITAL_Node):
        haleyChatCreditEventStatusURI: str
        haleyChatCreditEventTypeURI: str
        haleyChatCreditEventUpdateDateTime: datetime
        haleyChatCreditURI: str
        haleyChatCustomerIdentifier: str
        haleyChatQuotaCreditAmount: int
        haleyChatStripeInvoiceId: str
        accountURI: str

