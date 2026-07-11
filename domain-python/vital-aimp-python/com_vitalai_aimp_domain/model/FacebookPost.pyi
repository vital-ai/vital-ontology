
import datetime
from com_vitalai_domain_nlp.model.Document import Document


class FacebookPost(Document):
        commentsCount: int
        likesCount: int
        thumbnailImageFileNodeURI: str
        thumbnailImageURL: str

