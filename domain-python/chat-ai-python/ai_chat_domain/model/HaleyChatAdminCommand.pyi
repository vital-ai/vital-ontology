
import datetime
from com_vitalai_haley_domain.model.HaleyRequestMessage import HaleyRequestMessage


class HaleyChatAdminCommand(HaleyRequestMessage):
        haleyChatCollectionTypeURI: str
        haleyChatCommandObjectURI: str
        haleyChatCommandTypeURI: str
        haleyChatTargetAccountURI: str
        haleyChatTargetLoginURI: str
        testCaseString: str
        testCaseMessage: bool

