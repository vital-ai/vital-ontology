
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Sms(VITAL_Node):
        bodyPlain: str
        dateSent: datetime
        messageID: str
        recipient: str
        sender: str
        mms: bool

