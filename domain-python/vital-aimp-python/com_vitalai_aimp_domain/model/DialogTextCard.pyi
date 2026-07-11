
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class DialogTextCard(Card):
        conditionalLogic: str
        sectionHeaderHTML: str
        text: str
        questionCountExcluded: bool

