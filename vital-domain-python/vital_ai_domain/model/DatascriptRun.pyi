
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class DatascriptRun(VITAL_Node):
        jobID: str
        jobStatus: str
        lastModifiedDate: datetime
        scriptPath: str

