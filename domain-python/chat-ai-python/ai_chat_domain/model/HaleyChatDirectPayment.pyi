
import datetime
from ai_chat_domain.model.HaleyChatPayment import HaleyChatPayment


class HaleyChatDirectPayment(HaleyChatPayment):
        haleyChatDirectPaymentAppliedCreditURI: str
        haleyChatDirectPaymentAppliedDateTime: datetime
        haleyChatDirectPaymentAppliedStatusURI: str
        haleyChatDirectPaymentAppliedSubscriptionURI: str

