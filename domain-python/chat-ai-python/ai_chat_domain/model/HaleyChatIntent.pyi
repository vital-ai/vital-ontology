
import datetime
from com_vitalai_haley_domain.model.HaleyIntentCommand import HaleyIntentCommand


class HaleyChatIntent(HaleyIntentCommand):
        agentVariantURI: str
        streamModelResults: bool

