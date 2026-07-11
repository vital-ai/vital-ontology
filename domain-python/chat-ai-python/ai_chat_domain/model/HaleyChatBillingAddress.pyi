
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatBillingAddress(VITAL_Node):
        haleyChatAddressNormalizationStatusURI: str
        haleyChatBillingCity: str
        haleyChatBillingCountryURI: str
        haleyChatBillingCustomerEmail: str
        haleyChatBillingCustomerName: str
        haleyChatBillingName: str
        haleyChatBillingPostalCode: str
        haleyChatBillingProvinceURI: str
        haleyChatBillingRegion: str
        haleyChatBillingStateURI: str
        haleyChatBillingStreetAddress1: str
        haleyChatBillingStreetAddress2: str
        haleyChatBillingTelephoneContact: str
        haleyChatGooglePlaceURI: str
        haleyChatTelephoneTypeURI: str
        haleyChatBillingAddressInitialized: bool
        primaryBillingAddress: bool
        haleyCountryISOCode: str

