
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class VoiceMessage(VITAL_Node):
        bodyPlain: str
        dateSent: datetime
        fileNodeURI: str
        messageID: str
        recipient: str
        sender: str

