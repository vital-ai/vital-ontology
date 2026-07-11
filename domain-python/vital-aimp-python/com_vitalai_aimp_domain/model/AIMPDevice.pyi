
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AIMPDevice(VITAL_Node):
        deviceID: str
        audioDevice: bool
        visualDevice: bool

