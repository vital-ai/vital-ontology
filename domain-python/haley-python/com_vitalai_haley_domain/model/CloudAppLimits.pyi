
import datetime
from com_vitalai_haley_domain.model.HaleyCloud import HaleyCloud


class CloudAppLimits(HaleyCloud):
        dailyCostLimit: int
        dailyRequestGenerationLimit: int
        dailyRequestInputLimit: int
        dailyRequestLimit: int

