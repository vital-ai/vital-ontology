
import datetime
from com_vitalai_domain_nlp.model.Document import Document


class EmailMessage(Document):
        accountURI: str
        attachmentsCount: int
        bccRecipients: str
        bodyHtml: str
        bodyPlain: str
        category: str
        ccRecipients: str
        deliveryDate: datetime
        eMailTagURI: str
        eventTimestamp: int
        messageID: str
        optionalData: str
        recipients: str
        sender: str
        subject: str
        read: bool
        trackingOpens: bool

