
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class ArticleObject(Card):
        imageFileNodeURI: str
        imageURL: str
        publicationDate: datetime
        searchString: str
        shortDescription: str
        thumbnailImageFileNodeURI: str
        thumbnailImageURL: str
        title: str
        url: str

