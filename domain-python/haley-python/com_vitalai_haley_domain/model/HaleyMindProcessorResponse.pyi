
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyMindProcessorResponse(VITAL_Node):
        errorCode: int
        haleyMindContextIdentifier: str
        haleyMindProcessorResponseTypeURI: str
        processorRequestURI: str
        statusOk: bool
        errorMessage: str

