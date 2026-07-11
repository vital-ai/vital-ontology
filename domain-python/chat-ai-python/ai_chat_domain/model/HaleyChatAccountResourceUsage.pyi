
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatAccountResourceUsage(VITAL_Node):
        resourceUsageGigabyteTotalStorage: float
        resourceUsageS3GigabyteTotalStorage: float
        resourceUsageS3TotalFileCount: int
        resourceUsageTaskCompleteDateTime: datetime
        resourceUsageTotalFileCount: int
        resourceUsageUpdateDateTime: datetime
        resourceUsageCurrentUpdate: bool

