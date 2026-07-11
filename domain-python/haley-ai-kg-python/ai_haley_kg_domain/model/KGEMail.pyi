
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGEMail(KGNode):
        kGEMailType: str
        kGEmailBCCAddressList: str
        kGEmailCCAddressList: str
        kGEmailRecipientAddress: str
        kGEmailRecipientName: str
        kGEmailSendDateTime: datetime
        kGEmailSenderAddress: str
        kGEmailSenderName: str
        kGEmailSubject: str
        kGEmailSummary: str
        kGEmailToAddressList: str

