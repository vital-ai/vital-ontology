
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Document(VITAL_Node):
        analyzedBody: str
        analyzedTitle: str
        body: str
        contentID: str
        contentTag: str
        dmozPath: str
        documentPublicationDate: datetime
        documentSourceName: str
        documentTitle: str
        documentUrl: str
        documentUrlRoot: str
        extractedText: str
        extractedTitle: str
        lang: str
        sentimentScore: float
        slug: str
        sourceDomain: str
        sentimentMixed: bool

