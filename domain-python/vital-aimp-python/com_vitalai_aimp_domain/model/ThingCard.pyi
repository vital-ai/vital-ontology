
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class ThingCard(Card):
        address: str
        cardHeader: str
        directionsEndAddress: str
        directionsJSONResponse: str
        directionsStartAddress: str
        formattedContent: str
        imageCaption: str
        imageFileNodeURI: str
        imageURL: str
        latitude: float
        longitude: float
        neLatitude: float
        neLongitude: float
        payload: str
        publicationDate: datetime
        searchString: str
        shortDescription: str
        swLatitude: float
        swLongitude: float
        thumbnailImageFileNodeURI: str
        thumbnailImageURL: str
        title: str
        url: str
        zoomLevel: float
        autosaveOnChange: bool
        detailsEnabled: bool
        editing: bool

