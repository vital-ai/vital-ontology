
import datetime
from ai_chat_domain.model.HaleyChatAdminCommand import HaleyChatAdminCommand


class SendEmailAdminRequest(HaleyChatAdminCommand):
        emailDeliveryScheduleURI: str
        emailSendMethodURI: str

