
import datetime
from ai_chat_domain.model.HaleyChatAlert import HaleyChatAlert


class HaleyChatAccountOwnershipChangeAlert(HaleyChatAlert):
        haleyChatAccountModificationDestinationURI: str
        haleyChatAccountModificationSourceURI: str

