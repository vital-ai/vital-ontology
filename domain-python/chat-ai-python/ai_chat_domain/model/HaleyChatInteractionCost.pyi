
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatInteractionCost(VITAL_Node):
        haleyChatInteractionModelTypeURI: str
        haleyChatInteractionTypeURI: str
        haleyChatPaymentCurrencyURI: str
        interactionCostCreditAmount: int
        interactionCostPer1kInputTokenAmount: float
        interactionCostPer1kOutputTokenAmount: float

