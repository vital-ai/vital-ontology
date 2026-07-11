
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class TagElement(VITAL_Node):
        endPosition: int
        startPosition: int
        tagValue: str
        closingTag: bool
        openingTag: bool
        standaloneTag: bool

