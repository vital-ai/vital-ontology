
import datetime
from com_vitalai_haley_domain.model.HaleyMindRequest import HaleyMindRequest


class ActorMindRequest(HaleyMindRequest):
        actorSequence: str
        streamModelResults: bool

