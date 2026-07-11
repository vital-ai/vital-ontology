
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class PaymentConfirmation(Card):
        amount: float
        avatarURL: str
        currencySymbol: str
        recipient: str
        title: str
        url: str
        currencyISymbolnFrontOf: bool
        urlAvailable: bool

