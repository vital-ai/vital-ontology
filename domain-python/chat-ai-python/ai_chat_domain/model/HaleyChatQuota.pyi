
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatQuota(VITAL_Node):
        haleyChatQuotaAmount: int
        haleyChatQuotaCreditAmount: int
        haleyChatQuotaDate: datetime
        haleyChatQuotaSubscriptionAmount: int
        haleyChatQuotaSubscriptionBalance: int

