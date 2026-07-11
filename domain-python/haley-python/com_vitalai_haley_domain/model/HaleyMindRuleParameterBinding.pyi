
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyMindRuleParameterBinding(VITAL_Node):
        binaryParameterBinding: str
        booleanParameterBinding: bool
        dateTimeParameterBinding: datetime
        doubleParameterBinding: float
        integerParameterBinding: int
        listBinaryParameterBinding: str
        listBooleanParameterBinding: bool
        listDateTimeParameterBinding: datetime
        listDoubleParameterBinding: float
        listIntegerParameterBinding: int
        listStringParameterBinding: str
        listURIParameterBinding: str
        parameterBindingVariable: str
        stringParameterBinding: str
        uRIParameterBinding: str

