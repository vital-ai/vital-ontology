
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyWeatherType(VITAL_Node):
        weatherTypeDescriptor: str
        weatherTypeIndex: int
        weatherTypeLargeIconPath: str
        weatherTypeMediumIconPath: str
        weatherTypeSmallIconPath: str

