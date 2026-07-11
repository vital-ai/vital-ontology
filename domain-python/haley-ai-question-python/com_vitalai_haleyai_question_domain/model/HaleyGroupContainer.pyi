
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyGroupContainer(VITAL_Node):
        containerGroupURI: str
        containerRootURI: str
        containerUpdateTime: datetime
        haleyGroupBase: str
        haleyGroupBaseVersion: str
        haleyParameterURI: str
        haleyTaxonomyBase: str
        haleyTaxonomyBaseVersion: str
        serializedContainer: str
        serializedContainerJSON: str
        compressed: bool

