
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class CalendarEntry(VITAL_Node):
        endDate: datetime
        shortDescription: str
        startDate: datetime

