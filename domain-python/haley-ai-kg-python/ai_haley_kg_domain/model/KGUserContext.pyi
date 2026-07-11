
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class KGUserContext(VITAL_Node):
        kGPlaceURI: str
        kGUserContextAccountLevel: str
        kGUserContextAccountURI: str
        kGUserContextAgentFamiliarity: str
        kGUserContextAgentTone: str
        kGUserContextCurrentDateTime: datetime
        kGUserContextCurrentTimezone: str
        kGUserContextExperienceLevel: str
        kGUserContextGender: str
        kGUserContextLightLevel: float
        kGUserContextLocation: str
        kGUserContextLoginURI: str
        kGUserContextMood: str
        kGUserContextName: str
        kGUserContextPronoun: str
        kGUserContextSoundLevel: float

