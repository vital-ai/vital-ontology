
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyMindRequest(VITAL_Node):
        commandChildEndDateTime: datetime
        commandChildReceivedDateTime: datetime
        commandChildSentDateTime: datetime
        commandProcessorEndDateTime: datetime
        commandProcessorNotificationChannelURI: str
        commandProcessorReceivedDateTime: datetime
        commandProcessorSentDateTime: datetime
        commandReceivedDateTime: datetime
        commandSentDateTime: datetime
        commandStartDateTime: datetime
        haleyMindAgentInstanceURI: str
        processorCommandConsumerID: str
        processorCommandConsumerPartition: str
        processorCommandConsumerPartitionAssignmentList: str
        processorCommandEndDateTime: datetime
        processorCommandReceivedDateTime: datetime
        processorCommandSentDateTime: datetime

