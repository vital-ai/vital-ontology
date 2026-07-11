
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatQuotaTransactionEntry(VITAL_Node):
        chatTimestamp: datetime
        haleyChatInteractionURI: str
        haleyChatMessageURI: str
        haleyChatQuotaTransactionEntryStatusURI: str
        haleyChatQuotaTransactionEntryTypeURI: str
        haleyChatQuotaTransactionStatusURI: str
        haleyChatQuotaTransactionURI: str
        haleyChatTaskURI: str
        quotaCreditDebit: int
        quotaDebit: int
        quotaSubscriptionBalance: int
        quotaSubscriptionCreditBalance: int
        quotaSubscriptionDebit: int
        quotaTransactionNonce: str
        accountURI: str
        loginURI: str

