
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAnswerTypeClassMapping(VITAL_Node):
        answerTypePropertyValueConstraintString: str
        answerTypePropertyValueConstraintURI: str
        haleyMappingFunctionURI: str
        haleyMappingTypeURI: str
        mappedAnswerTypeURI: str
        mappedConstantStringValue: str
        mappedConstantURI: str

