
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Task(VITAL_Node):
        accountURI: str
        channelURI: str
        userID: str
        lLastRunTimestamp: int

