
import datetime
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class HaleyImageMessage(HaleyMessage):
        imageURL: str
        publicationDate: datetime
        searchString: str
        shortDescription: str
        thumbnailImageURL: str
        title: str
        url: str

