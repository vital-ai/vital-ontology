
import datetime
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class HaleyResponseMessage(HaleyMessage):
        affectedResourceCount: int
        commandChildEndDateTime: datetime
        commandChildReceivedDateTime: datetime
        commandChildSentDateTime: datetime
        commandEndDateTime: datetime
        commandProcessorEndDateTime: datetime
        commandProcessorReceivedDateTime: datetime
        commandProcessorSentDateTime: datetime
        commandReceivedDateTime: datetime
        commandSentDateTime: datetime
        commandStartDateTime: datetime
        haleyAccessViolationDescription: str
        haleyAccessViolationTypeURI: str
        haleyProgressAmount: float
        haleyProgressPercentage: float
        haleyProgressStatusTypeURI: str
        haleyProgressUnitTypeURI: str
        haleyResponseTypeURI: str
        processorCommandConsumerID: str
        processorCommandConsumerPartition: str
        processorCommandConsumerPartitionAssignmentList: str
        processorCommandEndDateTime: datetime
        processorCommandReceivedDateTime: datetime
        processorCommandSentDateTime: datetime
        haleyStatusMessage: str
        haleyStatusTypeURI: str

