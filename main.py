from dotenv import load_dotenv
import os
from m3o_weather import Weather


load_dotenv()

M3O_API_TOKEN = os.getenv("M3O_API_TOKEN")

weather = Weather(api_key=M3O_API_TOKEN)
now = weather.now(location="Moscow")
forecast = weather.forecast(location="London", days=3)
print(f"{now=}")
print(f"{forecast=}")
