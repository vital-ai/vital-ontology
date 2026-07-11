
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyQuestion(VITAL_Node):
        haleyGroupDisplayTypeURI: str
        haleyLanguageType: str
        haleyQuestionStatus: str
        horizontalColumnAssignment: int
        questionAbbreviatedText: str
        questionFriendlyText: str
        questionGroupIndex: int
        questionIdentifier: str
        questionProfessionalText: str
        questionText: str
        dependencyEnabled: bool
        hiddenInGroupDisplay: bool
        hiddenInPopform: bool
        hiddenQuestion: bool
        includeInSectionPopform: bool
        notificationContent: bool
        rowNameQuestion: bool
        description: str
        longDescription: str

