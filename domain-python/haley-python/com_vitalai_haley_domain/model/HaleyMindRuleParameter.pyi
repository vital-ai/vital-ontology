
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyMindRuleParameter(VITAL_Node):
        ruleParameterClassRestrictionURI: str
        ruleParameterIndex: int
        ruleParameterModeURI: str
        ruleParameterName: str
        ruleParameterResolveObject: bool
        ruleParameterResolveObjectGraph: bool
        ruleParameterResolveObjectList: bool
        ruleParameterTypeURI: str

