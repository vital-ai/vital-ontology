
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatQuotaReservation(VITAL_Node):
        chatTimestamp: datetime
        estimatedInputTokenCount: int
        estimatedModelCost: float
        estimatedOutputTokenCount: int
        estimatedQuotaDebit: int
        haleyChatInteractionModelProviderURI: str
        haleyChatInteractionModelTypeURI: str
        haleyChatInteractionURI: str
        haleyChatMessageURI: str
        haleyChatQuotaReservationStatusURI: str
        haleyChatStatusMessage: str
        haleyChatTaskURI: str
        accountURI: str
        loginURI: str

