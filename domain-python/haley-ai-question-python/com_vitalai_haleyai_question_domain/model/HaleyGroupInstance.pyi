
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyGroupInstance(VITAL_Node):
        haleyGroup: str
        haleyGroupBase: str
        haleyGroupBaseVersion: str
        instanceOriginAccount: str
        instanceOriginLoginURI: str
        instanceOriginSessionID: str
        instanceOriginTimestamp: datetime
        instanceTimestamp: datetime
        provenanceInstanceURI: str
        ableToRemoveGroup: bool
        activeInstance: bool
        inconsistentGroupInstance: bool
        selectedGroupInstance: bool
        suppressEmptyAnswerValues: bool

