
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class MapObject(Card):
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

