
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatQuotaTransaction(VITAL_Node):
        chatTimestamp: datetime
        estimatedModelCost: float
        haleyChatInteractionModelProviderURI: str
        haleyChatInteractionModelTypeURI: str
        haleyChatInteractionURI: str
        haleyChatMessageURI: str
        haleyChatQuotaTransactionStatusURI: str
        haleyChatQuotaTransactionTypeURI: str
        haleyChatStatusMessage: str
        haleyChatTaskURI: str
        inputTokenCount: int
        outputTokenCount: int
        quotaCreditDebit: int
        quotaDebit: int
        quotaSubscriptionDebit: int
        quotaTransactionNonce: str
        accountURI: str
        loginURI: str

