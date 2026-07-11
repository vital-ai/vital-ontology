
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class PermitStreamingRequestMessage(AIMPMessage):
        permitStreamingAgentInstallURI: str
        permitStreamingRequestURI: str

