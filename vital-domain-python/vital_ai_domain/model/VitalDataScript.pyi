
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class VitalDataScript(VITAL_Node):
        lastCompilationError: str
        lastModifiedDate: datetime
        scriptPath: str
        vitalDataScriptBody: str
        adminScript: bool
        regularScript: bool
        appID: str
        organizationID: str

