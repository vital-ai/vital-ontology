
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyQuestionArray(VITAL_Node):
        haleyLanguageType: str
        questionAbbreviatedText: str
        questionFriendlyText: str
        questionGroupIndex: int
        questionIdentifier: str
        questionProfessionalText: str
        questionText: str
        description: str
        longDescription: str

