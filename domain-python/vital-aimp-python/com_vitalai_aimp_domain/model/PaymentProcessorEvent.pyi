
import datetime
from com_vitalai_aimp_domain.model.ProcessorEvent import ProcessorEvent


class PaymentProcessorEvent(ProcessorEvent):
        paymentProcessorEventId: str
        paymentProviderEventType: str

