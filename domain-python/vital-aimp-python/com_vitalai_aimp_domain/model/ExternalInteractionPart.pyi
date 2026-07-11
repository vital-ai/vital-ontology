
import datetime
from com_vitalai_aimp_domain.model.BaseInteractionPart import BaseInteractionPart


class ExternalInteractionPart(BaseInteractionPart):
        recipientReferenceURI: str
        senderReferenceURI: str

