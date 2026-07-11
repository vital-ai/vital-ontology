
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class WeatherForecast(Card):
        address: str
        latitude: float
        longitude: float
        searchString: str
        weatherJSONResponse: str

