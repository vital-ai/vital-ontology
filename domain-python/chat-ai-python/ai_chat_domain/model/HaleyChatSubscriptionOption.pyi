
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatSubscriptionOption(VITAL_Node):
        haleyChatContentJSON: str
        haleyChatContentObjectIcon: str
        haleyChatContentObjectOrder: int
        haleyChatContentObjectTypeURI: str
        haleyChatContentTitle: str
        haleyChatRequiredPromotionURI: str
        haleyChatSubscriptionLevelURI: str
        subscriptionPriceIdentifier: str
        subscriptionProductIdentifier: str
        haleyChatSubscriptionOptionAvailable: bool

