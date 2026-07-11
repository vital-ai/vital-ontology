
import datetime
from com_vitalai_haley_domain.model.HaleyRequestMessage import HaleyRequestMessage


class HaleyChatManagerCommand(HaleyRequestMessage):
        haleyChatCollectionTypeURI: str
        haleyChatCommandObjectURI: str
        haleyChatCommandTypeURI: str

