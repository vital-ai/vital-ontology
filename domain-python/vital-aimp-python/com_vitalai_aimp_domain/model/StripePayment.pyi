
import datetime
from com_vitalai_aimp_domain.model.Payment import Payment


class StripePayment(Payment):
        json: str
        token: str

