
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class KGIndexDocumentAttempt(VITAL_Node):
        documentAttemptDateTime: datetime
        documentAttemptStatus: str
        documentAttemptStatusCode: int
        documentCorrectedURL: str
        documentOriginalURL: str
        kGIndexDocumentAttemptStatusTypeURI: str

