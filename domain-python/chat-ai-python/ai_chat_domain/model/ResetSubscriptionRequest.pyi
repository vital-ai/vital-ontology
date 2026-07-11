
import datetime
from ai_chat_domain.model.HaleyChatCommand import HaleyChatCommand


class ResetSubscriptionRequest(HaleyChatCommand):
        haleyChatQuotaCreditAmount: int
        haleyChatQuotaSubscriptionAmount: int

