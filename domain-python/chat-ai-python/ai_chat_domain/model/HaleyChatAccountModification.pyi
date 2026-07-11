
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatAccountModification(VITAL_Node):
        accountModificationCreationDateTime: datetime
        accountModificationStatusMessage: str
        accountModificationTrackingIdentifier: str
        haleyChatAccountModificationAccountSourceURI: str
        haleyChatAccountModificationDestinationString: str
        haleyChatAccountModificationDestinationURI: str
        haleyChatAccountModificationLoginSourceURI: str
        haleyChatAccountModificationNewSubscriptionStatusURI: str
        haleyChatAccountModificationPriorSubscriptionStatusURI: str
        haleyChatAccountModificationSourceString: str
        haleyChatAccountModificationSourceURI: str
        haleyChatAccountModificationStatusURI: str
        haleyChatAccountModificationTypeURI: str
        haleyChatLoginRoleURI: str

