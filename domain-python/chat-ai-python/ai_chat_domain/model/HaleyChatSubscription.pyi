
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatSubscription(VITAL_Node):
        haleyChatSubscriptionEndDate: datetime
        haleyChatSubscriptionIdentifier: str
        haleyChatSubscriptionLevelURI: str
        haleyChatSubscriptionStartDate: datetime
        haleyChatSubscriptionStatusMessage: str
        haleyChatSubscriptionStatusURI: str
        haleyChatSubscriptionTermStatusURI: str
        haleyChatSubscriptionTrialEndDate: datetime
        haleyChatSubscriptionTrialStartDate: datetime
        haleyChatPaymentMethodActive: bool
        haleyChatSubscriptionInitialized: bool

