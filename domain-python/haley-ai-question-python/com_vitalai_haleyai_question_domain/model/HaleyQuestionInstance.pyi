
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyQuestionInstance(VITAL_Node):
        haleyQuestion: str
        instanceOriginAccount: str
        instanceOriginLoginURI: str
        instanceOriginSessionID: str
        instanceOriginTimestamp: datetime
        instanceTimestamp: datetime
        provenanceInstanceURI: str
        activeInstance: bool
        hiddenInGroupDisplay: bool

