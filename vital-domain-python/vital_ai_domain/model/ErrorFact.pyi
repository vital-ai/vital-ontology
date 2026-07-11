
import datetime
from vital_ai_domain.model.VITAL_Fact import VITAL_Fact


class ErrorFact(VITAL_Fact):
        errorMessage: str
        errorType: str

