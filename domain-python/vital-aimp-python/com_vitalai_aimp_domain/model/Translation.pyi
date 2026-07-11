
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class Translation(Card):
        sourceLanguage: str
        sourcePronounciation: str
        sourceText: str
        targetLanguage: str
        targetPronounciation: str
        targetText: str

