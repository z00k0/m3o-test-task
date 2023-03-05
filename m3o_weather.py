from dataclasses import dataclass, field
import datetime
import requests
import json
from typing import List


@dataclass
class WeatherNow:
    location: str
    region: str
    country: str
    latitude: float
    longitude: float
    timezone: str
    local_time: datetime.datetime
    temp_c: float
    temp_f: float
    feels_like_c: float
    feels_like_f: float
    humidity: int
    cloud: int
    daytime: bool
    condition: str
    icon_url: str
    wind_mph: float
    wind_kph: float
    wind_direction: str
    wind_degree: int

    def __post_init__(self):
        self.local_time = datetime.datetime.strptime(self.local_time, "%Y-%m-%d %H:%M")


@dataclass
class Forecast:
    date: datetime.datetime
    max_temp_c: float
    max_temp_f: float
    min_temp_c: float
    min_temp_f: float
    avg_temp_c: float
    avg_temp_f: float
    will_it_rain: bool
    chance_of_rain: int
    condition: str
    icon_url: str
    sunrise: datetime.datetime
    sunset: datetime.datetime
    max_wind_mph: float
    max_wind_kph: float

    def __post_init__(self):
        self.date = datetime.datetime.strptime(self.date, "%Y-%m-%d")
        self.sunrise = datetime.datetime.strptime(self.sunrise, "%H:%M %p").time()
        self.sunset = datetime.datetime.strptime(self.sunset, "%H:%M %p").time()


@dataclass
class WeatherForecast:
    location: str
    region: str
    country: str
    latitude: float
    longitude: float
    timezone: str
    local_time: datetime.datetime
    forecast: List[Forecast] = field(default_factory=list)

    def __post_init__(self):
        self.local_time = datetime.datetime.strptime(self.local_time, "%Y-%m-%d %H:%M")


class Weather:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        self.base_url = "https://api.m3o.com/v1/weather"

    def now(self, location: str) -> WeatherNow:
        url = self.base_url + "/now"
        data = {"location": location}
        try:
            resp = requests.post(url=url, data=json.dumps(data), headers=self.headers)
            resp.raise_for_status()
            resp_json = resp.json()

            return WeatherNow(**resp_json)

        except:
            raise
        # except requests.exceptions.RequestException as e:
        #     print(str(e))

    def forecast(self, location: str, days: int) -> WeatherForecast:
        url = self.base_url + "/forecast"
        data = {"location": location, "days": days}
        try:
            resp = requests.post(url=url, data=json.dumps(data), headers=self.headers)
            resp.raise_for_status()
            resp_json = resp.json()
            forecasts_dict = resp_json.pop("forecast")
            forecasts = [Forecast(**f) for f in forecasts_dict]

            return WeatherForecast(forecast=forecasts, **resp_json)

        except:
            raise
