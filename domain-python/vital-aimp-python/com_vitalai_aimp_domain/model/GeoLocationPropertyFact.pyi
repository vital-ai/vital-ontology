
import datetime
from com_vitalai_aimp_domain.model.PropertyFact import PropertyFact


class GeoLocationPropertyFact(PropertyFact):
        address: str
        geolocation: str

