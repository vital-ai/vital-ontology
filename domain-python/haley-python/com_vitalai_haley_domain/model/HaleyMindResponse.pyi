
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyMindResponse(VITAL_Node):
        affectedResourceCount: int
        commandChildEndDateTime: datetime
        commandChildReceivedDateTime: datetime
        commandChildSentDateTime: datetime
        commandProcessorEndDateTime: datetime
        commandProcessorReceivedDateTime: datetime
        commandProcessorSentDateTime: datetime
        commandReceivedDateTime: datetime
        commandSentDateTime: datetime
        commandStartDateTime: datetime
        haleyMindResponseStatusTypeURI: str
        mindResponseStatusMessage: str
        processorCommandConsumerID: str
        processorCommandConsumerPartition: str
        processorCommandConsumerPartitionAssignmentList: str
        processorCommandEndDateTime: datetime
        processorCommandReceivedDateTime: datetime
        processorCommandSentDateTime: datetime

