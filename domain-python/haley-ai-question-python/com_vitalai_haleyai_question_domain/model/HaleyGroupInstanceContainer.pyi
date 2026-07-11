
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyGroupInstanceContainer(VITAL_Node):
        containerGroupInstanceURI: str
        containerRootURI: str
        containerUpdateTime: datetime
        haleyGroupBase: str
        haleyGroupBaseVersion: str
        haleyParameterURI: str
        serializedContainer: str
        serializedContainerJSON: str
        compressed: bool

