
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatInteractionMessageRange(VITAL_Node):
        chatMessageRangeEndDateTime: datetime
        chatMessageRangeEndSequence: int
        chatMessageRangeMaxCount: int
        chatMessageRangeStartDateTime: datetime
        chatMessageRangeStartSequence: int
        haleyChatInteractionMessageRangeTypeURI: str
        haleyChatInteractionURI: str
        chatMessageRangeEndOpen: bool
        chatMessageRangeStartOpen: bool

