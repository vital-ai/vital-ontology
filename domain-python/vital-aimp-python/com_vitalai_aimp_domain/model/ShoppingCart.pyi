
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class ShoppingCart(Card):
        quantityData: str
        shippingFee: float
        tax: float

