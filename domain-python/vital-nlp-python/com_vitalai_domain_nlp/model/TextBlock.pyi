
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class TextBlock(VITAL_Node):
        textBlockLength: int
        textBlockOffset: int
        textBlockText: str
        transformationVector: str

