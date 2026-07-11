
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatTask(VITAL_Node):
        haleyChatCompletionTokenCount: int
        haleyChatInteractionURI: str
        haleyChatMessageURI: str
        haleyChatPromptTokenCount: int
        haleyChatTaskDeltaTime: int
        haleyChatTaskEndDateTime: datetime
        haleyChatTaskStartDateTime: datetime
        haleyChatTaskStatusURI: str
        haleyChatTaskTypeURI: str
        haleyChatTaskUpdateDateTime: datetime
        haleyChatTotalTokenCount: int

