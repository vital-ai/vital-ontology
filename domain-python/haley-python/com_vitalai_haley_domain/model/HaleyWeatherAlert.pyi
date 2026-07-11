
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyWeatherAlert(VITAL_Node):
        haleyWeatherAlertCertaintyURI: str
        haleyWeatherAlertSeverityURI: str
        weatherAlertDescription: str
        weatherAlertEvent: str
        weatherAlertExpiration: datetime
        weatherAlertHeadline: str
        weatherAlertOnset: datetime
        weatherAlertSender: str

