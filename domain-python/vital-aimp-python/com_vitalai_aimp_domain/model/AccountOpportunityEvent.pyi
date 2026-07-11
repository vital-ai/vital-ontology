
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AccountOpportunityEvent(VITAL_Node):
        accountOpportunityEventDateTime: datetime
        accountOpportunityEventIdentifier: str
        accountOpportunityEventTypeURI: str
        accountOpportunityURI: str

