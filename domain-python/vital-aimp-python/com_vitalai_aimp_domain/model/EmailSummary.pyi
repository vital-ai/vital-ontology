
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class EmailSummary(VITAL_Node):
        accountURI: str
        attachmentsCount: int
        bccRecipients: str
        bodyHtml: str
        bodyPlain: str
        category: str
        ccRecipients: str
        eMailTagURI: str
        eventTimestamp: int
        messageID: str
        recipients: str
        sender: str
        subject: str
        read: bool
        trackingOpens: bool

