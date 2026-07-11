
import datetime
from com_vitalai_haley_domain.model.HaleyProcessorRequest import HaleyProcessorRequest


class HaleyMindProcessorRequest(HaleyProcessorRequest):
        haleyMindAppURI: str
        haleyMindContextIdentifier: str
        haleyMindProcessorRequestTypeURI: str
        haleyMindServiceMetaQLName: str
        haleyMindServiceRequestTypeURI: str
        haleyMindServiceRuleName: str
        haleyMindServiceRuleURI: str
        inferenceQuery: str
        inferenceUpdate: str

