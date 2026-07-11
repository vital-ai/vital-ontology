
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AgentInstanceContainerDeployment(VITAL_Node):
        agentInstanceContainerDeploymentStatusTypeURI: str
        containerClusterName: str
        containerImageIdentifier: str
        containerLaunchDateTime: datetime
        containerLoadBalancerName: str
        containerLoadBalancerURL: str
        containerRepository: str
        containerServiceName: str
        containerStoppedDateTime: datetime
        containerTaskMaximumCount: int
        containerTaskMinimumCount: int
        containerTaskName: str

