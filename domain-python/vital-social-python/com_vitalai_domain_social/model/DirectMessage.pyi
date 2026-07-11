
import datetime
from com_vitalai_domain_nlp.model.Document import Document


class DirectMessage(Document):
        authorID: int
        authorName: str
        authorScreenName: str
        directMessageID: int
        recipientID: int
        recipientName: str
        recipientScreenName: str

