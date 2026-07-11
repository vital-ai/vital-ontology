
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatCredit(VITAL_Node):
        creditPaidDateTime: datetime
        creditedDateTime: datetime
        haleyChatCreditStatusURI: str
        haleyChatQuotaCreditAmount: int

