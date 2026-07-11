
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyRowInstance(VITAL_Node):
        haleyBeliefModeURI: str
        haleyRow: str
        haleyRowInstanceDerivationTypeURI: str
        haleyRowTypeURI: str
        instanceOriginAccount: str
        instanceOriginLoginURI: str
        instanceOriginSessionID: str
        instanceOriginTimestamp: datetime
        instanceTimestamp: datetime
        provenanceInstanceURI: str
        referenceObjectURI: str
        rowInstanceCounter: str
        ableToBeDeleted: bool
        activeInstance: bool
        hiddenInGroupDisplay: bool
        readOnlyRowValue: bool
        secondarySource: bool
        selectedRowInstance: bool
        suppressEmptyAnswerValues: bool

