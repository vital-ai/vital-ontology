
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAnswerTypeMapping(VITAL_Node):
        destinationConditionalBooleanValue: bool
        destinationConditionalDateValue: datetime
        destinationConditionalDoubleValue: float
        destinationConditionalIntegerValue: int
        destinationConditionalLongValue: int
        destinationConditionalStringValue: str
        destinationConditionalURIValueURI: str
        destinationMappedAnswerTypeURI: str
        haleyMappingFunctionURI: str
        haleyMappingTypeURI: str
        mappingComparableType: str
        sourceConditionalBooleanValue: bool
        sourceConditionalDateValue: datetime
        sourceConditionalDoubleValue: float
        sourceConditionalIntegerValue: int
        sourceConditionalLongValue: int
        sourceConditionalStringValue: str
        sourceConditionalURIValueURI: str
        sourceConditionalUpperDateValue: datetime
        sourceConditionalUpperDoubleValue: float
        sourceConditionalUpperIntegerValue: int
        sourceConditionalUpperLongValue: int
        sourceConditionalUpperStringValue: str
        sourceMappedAnswerTypeURI: str

