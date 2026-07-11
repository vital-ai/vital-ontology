
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyTask(VITAL_Node):
        defaultRecurrenceTime: int
        exceptionMessage: str
        lastAttemptTime: datetime
        owner: str
        scheduledExecutionTime: datetime
        topPriority: bool
        stackTrace: str
        status: str
        statusMessage: str

