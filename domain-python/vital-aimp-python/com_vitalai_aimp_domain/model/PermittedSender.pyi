
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class PermittedSender(VITAL_Node):
        email: str
        permittedSenderStatusURI: str
        permittedSenderTypeURI: str

