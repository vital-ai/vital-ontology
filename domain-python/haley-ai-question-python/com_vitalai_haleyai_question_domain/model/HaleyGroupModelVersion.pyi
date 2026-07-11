
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyGroupModelVersion(VITAL_Node):
        haleyGroupBase: str
        haleyGroupBaseVersion: str
        haleyGroupModelURI: str
        haleyGroupModelVersionActivateDate: datetime
        haleyGroupModelVersionDeactivateDate: datetime
        activeGroupModelVersion: bool

