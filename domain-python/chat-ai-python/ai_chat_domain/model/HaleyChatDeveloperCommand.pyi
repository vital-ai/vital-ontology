
import datetime
from com_vitalai_haley_domain.model.HaleyRequestMessage import HaleyRequestMessage


class HaleyChatDeveloperCommand(HaleyRequestMessage):
        haleyChatCollectionTypeURI: str
        haleyChatCommandObjectURI: str
        haleyChatCommandTypeURI: str

