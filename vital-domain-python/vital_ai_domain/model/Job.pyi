
import datetime
from vital_ai_domain.model.VitalDataScript import VitalDataScript


class Job(VitalDataScript):
        cronExpression: str
        interval: int
        intervalTimeUnit: str
        lastExecutionTime: datetime
        nextExecutionTime: datetime
        callable: bool
        paused: bool

