
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyMindQuery(VITAL_Node):
        haleyMindAppURI: str
        haleyMindInferenceQuery: str
        haleyMindQueryErrorCode: int
        haleyMindQueryErrorMessage: str
        haleyMindQueryModule: str
        haleyMindQueryParameters: str
        haleyMindQueryStatusURI: str
        queryToRuleURI: str

