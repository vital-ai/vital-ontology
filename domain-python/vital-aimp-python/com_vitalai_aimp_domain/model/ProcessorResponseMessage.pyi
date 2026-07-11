
import datetime
from com_vitalai_aimp_domain.model.ProcessorMessage import ProcessorMessage


class ProcessorResponseMessage(ProcessorMessage):
        processorResponseTypeURI: str
        status: str
        statusMessage: str

