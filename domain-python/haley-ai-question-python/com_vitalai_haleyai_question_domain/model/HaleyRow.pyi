
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyRow(VITAL_Node):
        haleyGroupDisplayTypeURI: str
        haleyLanguageType: str
        haleyRowTypeURI: str
        mappingObjectName: str
        questionAbbreviatedText: str
        questionFriendlyText: str
        questionGroupIndex: int
        questionProfessionalText: str
        questionText: str
        rowCounter: str
        rowHorizontalColumnNameList: str
        rowHorizontalMaxColumns: int
        rowID: str
        rowIndex: int
        associatedWithMapping: bool
        calculatedRowValue: bool
        hiddenInGroupDisplay: bool
        readOnlyRowValue: bool

