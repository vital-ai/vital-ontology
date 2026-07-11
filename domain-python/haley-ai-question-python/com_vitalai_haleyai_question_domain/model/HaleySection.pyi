
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleySection(VITAL_Node):
        sectionIndex: int
        hiddenInGroupDisplay: bool
        includedWhenEmpty: bool
        skipEmptyQuestions: bool
        skipEmptyRows: bool

