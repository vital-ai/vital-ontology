
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class PushNotification(VITAL_Node):
        expirationDate: datetime
        badge: int
        optionalData: str
        sound: str
        text: str
        tokens: str

