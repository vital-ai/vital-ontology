
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyContainer(VITAL_Node):
        containerRootURI: str
        containerSortOrder: int
        containerUpdateTime: datetime
        haleyContainerAnswerSetURI: str
        haleyContainerScopeTypeURI: str
        haleyContainerTypeURI: str
        haleyParameterURI: str
        haleyQueryName: str
        serializedContainer: str
        serializedContainerJSON: str
        compressed: bool

