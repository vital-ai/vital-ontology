
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyDialogMapping(VITAL_Node):
        dialogProfileURI: str
        dialogText: str
        mappedEdgeClassURI: str
        mappedNodeClassURI: str
        mappedNodeInstanceURI: str
        mappingType: str
        normalizedText: str

