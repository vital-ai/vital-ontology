
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAnswerValueMapping(VITAL_Node):
        destinationMappedAnswerTypeURI: str
        haleyMappedObjectURI: str
        haleyMappedRowTypeURI: str
        haleyMappedRowURI: str
        sourceMappedAnswerTypeURI: str

