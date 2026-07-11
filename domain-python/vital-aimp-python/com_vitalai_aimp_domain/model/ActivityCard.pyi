
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class ActivityCard(Card):
        activityItemJSON: str
        activityMessage: str
        activityTaskIdentifier: str
        activityCancelEnabled: bool
        activityCanceled: bool
        activityComplete: bool
        activitySpinnerEnabled: bool

