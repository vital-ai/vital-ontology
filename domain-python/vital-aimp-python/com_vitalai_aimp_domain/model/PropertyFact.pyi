
import datetime
from vital_ai_domain.model.VITAL_Fact import VITAL_Fact


class PropertyFact(VITAL_Fact):
        factScope: str
        propertyName: str
        propertyValue: str

