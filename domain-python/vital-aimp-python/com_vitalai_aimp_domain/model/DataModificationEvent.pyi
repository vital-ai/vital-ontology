
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class DataModificationEvent(VITAL_Node):
        accountURI: str
        classURI: str
        eventType: str
        objectURI: str
        queueName: str

