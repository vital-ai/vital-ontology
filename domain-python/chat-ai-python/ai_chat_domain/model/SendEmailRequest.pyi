
import datetime
from ai_chat_domain.model.HaleyChatCommand import HaleyChatCommand


class SendEmailRequest(HaleyChatCommand):
        emailDeliveryScheduleURI: str
        emailSendMethodURI: str

