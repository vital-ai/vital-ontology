
import datetime
from com_vitalai_aimp_domain.model.AIMPThing import AIMPThing


class Payment(AIMPThing):
        address: str
        chargeAmount: int
        currencySymbol: str
        fullName: str
        id: str

