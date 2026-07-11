
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class ErrorNode(VITAL_Node):
        accountURI: str
        messageSerialized: str
        queueName: str
        stackTrace: str
        text: str

