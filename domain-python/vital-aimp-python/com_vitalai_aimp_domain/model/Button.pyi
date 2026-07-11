
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Button(VITAL_Node):
        buttonType: str
        id: str
        payload: str
        url: str
        selected: bool

