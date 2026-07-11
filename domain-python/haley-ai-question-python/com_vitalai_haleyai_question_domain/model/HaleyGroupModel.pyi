
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyGroupModel(VITAL_Node):
        currentHaleyGroupModelVersion: str
        currentHaleyGroupModelVersionURI: str
        haleyGroupBase: str
        haleyGroupModelActivateDate: datetime
        haleyGroupModelDeactivateDate: datetime
        activeGroupModel: bool

