
import datetime
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class HaleyArticleMessage(HaleyMessage):
        imageURL: str
        longDescription: str
        publicationDate: datetime
        searchString: str
        shortDescription: str
        thumbnailImageURL: str
        title: str
        url: str

