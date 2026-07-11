
import datetime
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class HaleyMapMessage(HaleyMessage):
        address: str
        directionsEndAddress: str
        directionsJSONResponse: str
        directionsStartAddress: str
        latitude: float
        longitude: float
        neLatitude: float
        neLongitude: float
        searchString: str
        swLatitude: float
        swLongitude: float
        zoomLevel: float

