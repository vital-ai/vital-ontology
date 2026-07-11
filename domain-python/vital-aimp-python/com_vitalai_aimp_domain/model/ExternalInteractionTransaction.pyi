
import datetime
from com_vitalai_aimp_domain.model.BaseInteractionTransaction import BaseInteractionTransaction


class ExternalInteractionTransaction(BaseInteractionTransaction):
        externalInteractionFee: float
        externalInteractionTotalFee: float

