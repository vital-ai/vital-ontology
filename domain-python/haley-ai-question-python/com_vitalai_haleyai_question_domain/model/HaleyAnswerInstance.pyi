
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAnswerInstance(VITAL_Node):
        answerInstanceInteractionTypeURI: str
        answerValue: str
        enhancementRuleSourceURI: str
        fallbackAnswerValue: str
        fallbackAnswerValueEncoding: str
        haleyAnswer: str
        haleyAnswerConstantURI: str
        haleyAnswerFollowupType: str
        haleyAnswerInstanceDependencyStatus: str
        haleyAnswerInstanceDerivationTypeURI: str
        haleyAnswerType: str
        haleyBeliefModeURI: str
        haleyMappedAnswerInstance: str
        instanceOriginAccount: str
        instanceOriginLoginURI: str
        instanceOriginSessionID: str
        instanceOriginTimestamp: datetime
        instanceTimestamp: datetime
        provenanceInstanceURI: str
        activeInstance: bool
        readOnlyAnswerValue: bool
        secondarySource: bool
        suppressEmptyAnswerValues: bool

