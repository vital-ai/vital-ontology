
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatPaymentMethod(VITAL_Node):
        haleyChatPaymentMethodAddedDate: datetime
        haleyChatPaymentMethodCountryURI: str
        haleyChatPaymentMethodExpirationDate: datetime
        haleyChatPaymentMethodExpirationMonth: int
        haleyChatPaymentMethodExpirationYear: int
        haleyChatPaymentMethodHash: str
        haleyChatPaymentMethodIdentifier: str
        haleyChatPaymentMethodIssuingBankName: str
        haleyChatPaymentMethodLastDigits: str
        haleyChatPaymentMethodName: str
        haleyChatPaymentMethodStatusURI: str
        haleyChatPaymentMethodTypeURI: str
        haleyChatPaymentNetworkURI: str
        haleyChatPaymentMethodDefault: bool
        haleyCountryISOCode: str

