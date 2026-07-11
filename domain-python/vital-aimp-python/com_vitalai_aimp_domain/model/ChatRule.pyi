
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class ChatRule(VITAL_Node):
        chatRuleID: int
        chatRulePattern: str
        chatRuleResponse: str
        chatRuleSetURI: str

