
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class OpenIFrame(Card):
        endpointURI: str
        intent: str
        propertyValue: str
        purgeSession: bool

