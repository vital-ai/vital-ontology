
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class KGServiceEvent(VITAL_Node):
        kGServiceEventMetaJSON: str
        kGServiceEventSpaceIdentifier: str
        kGServiceEventTimestamp: datetime
        kGServiceEventUUID: str
        kGServiceEventUsername: str
        kGServiceURI: str

