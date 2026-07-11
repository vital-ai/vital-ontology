
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Card(VITAL_Node):
        aIMPMessageContentURI: str
        cardText: str
        index: float
        sendAsAttachment: bool

