
import datetime
from com_vitalai_aimp_domain.model.UserCommandMessage import UserCommandMessage


class HaleyRequestMessage(UserCommandMessage):
        commandChildEndDateTime: datetime
        commandChildReceivedDateTime: datetime
        commandChildSentDateTime: datetime
        commandProcessorEndDateTime: datetime
        commandProcessorReceivedDateTime: datetime
        commandProcessorSentDateTime: datetime
        commandReceivedDateTime: datetime
        commandSentDateTime: datetime
        commandStartDateTime: datetime
        processorCommandConsumerID: str
        processorCommandConsumerPartition: str
        processorCommandConsumerPartitionAssignmentList: str
        processorCommandEndDateTime: datetime
        processorCommandReceivedDateTime: datetime
        processorCommandSentDateTime: datetime

