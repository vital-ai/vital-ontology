
import datetime
from com_vitalai_haley_domain.model.HaleyRequestMessage import HaleyRequestMessage


class HaleyChatCommand(HaleyRequestMessage):
        haleyChatCollectionTypeURI: str
        haleyChatCommandObjectURI: str
        haleyChatCommandTypeURI: str
        testCaseString: str
        testCaseMessage: bool

