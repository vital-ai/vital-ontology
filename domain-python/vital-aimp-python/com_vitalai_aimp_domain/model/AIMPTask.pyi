
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AIMPTask(VITAL_Node):
        aIMPMessageContentURI: str
        aIMPTaskProgressURI: str
        aIMPTaskStatusURI: str
        aIMPTaskTypeURI: str
        chatCompletionTokenCount: int
        chatPromptTokenCount: int
        chatTaskDeltaTime: int
        chatTaskEndDateTime: datetime
        chatTaskStagesJSON: str
        chatTaskStartDateTime: datetime
        chatTaskUpdateDateTime: datetime
        chatTotalTokenCount: int
        messageURI: str
        timezone: str
        daylightSavingsTime: bool

