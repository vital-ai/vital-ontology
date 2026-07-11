
import datetime
from com_vitalai_haley_domain.model.HaleyRegion import HaleyRegion


class HaleyUSPostalRegion(HaleyRegion):
        countyRegionURI: str
        divisionRegionURI: str
        fIPSCode: str
        postalCode: str
        postalCodePlusFour: str
        timeZoneIdentifier: str

