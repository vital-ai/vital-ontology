
import datetime
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class HaleyWeatherMessage(HaleyMessage):
        address: str
        latitude: float
        longitude: float
        searchString: str
        weatherJSONResponse: str

