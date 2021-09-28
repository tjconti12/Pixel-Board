import pyowm
import constants

owm = pyowm.OWM(constants.api_key)
observation = owm.weather_at_place('Brooklyn')
w = observation.get_weather()
temp = w.get_temperature('fahrenheit')
print(temp)