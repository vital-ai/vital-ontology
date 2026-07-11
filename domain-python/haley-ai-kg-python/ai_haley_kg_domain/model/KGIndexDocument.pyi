
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class KGIndexDocument(VITAL_Node):
        documentAuthorList: str
        documentContentPath: str
        documentContentType: str
        documentCorrectedURL: str
        documentDescription: str
        documentHTMLContent: str
        documentHeadline: str
        documentOriginalURL: str
        documentPublicationDateTime: datetime
        documentRetrievalDateTime: datetime
        documentURL: str
        documentVersion: str
        kGIndexDocumentClassificationURI: str
        kGIndexDocumentStatusURI: str
        kGIndexDocumentStorageTypeURI: str

