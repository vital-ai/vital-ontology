
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class DialogButton(Card):
        conditionalLogic: str
        id: str
        sectionHeaderHTML: str
        questionCountExcluded: bool

