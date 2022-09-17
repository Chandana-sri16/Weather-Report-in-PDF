"""
Team- 2 Weather Forecast Project
weather info of desired cities
output format - PDF file
"""

import requests
from datetime import datetime
import pytz
from input import user_input

# openweather website
apikey1 = "2f4c7114074ebece0db1c34dd91f2db3"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="

# weatherbit website
apikey2 = "f385a5578ffb45bd9403ee88e651c4f3"
base_url2 = "https://api.weatherbit.io/v2.0/current?"

# # goweather website
# base_url3 = "https://goweather.herokuapp.com/weather/"

while True:
    try:
        # # city names
        city = input("\nEnter city name:- ").upper()
        print("Fetching info....")

        # full url and getting json format for given city
        # openweather website
        full_url = base_url + city + "&appid=" + apikey1
        data = requests.get(full_url).json()

        # weatherbit website
        full_url2 = base_url2 + "&key=" + apikey2 + "&city=" + city
        data2 = requests.get(full_url2).json()

        # goweather website
        # full_url3 = base_url3 + city
        # data3 = requests.get(full_url3).json()

        timeZ_Kl = pytz.timezone('Asia/kolkata')      # current time and date
        dt_Kl = datetime.now(timeZ_Kl)

        # fetching info from the json format using keys
        # openweather website variables
        temp_max = int(data['main']['feels_like'] - 273.15)
        temp_min = int(data['main']['temp_min'] - 273.15)
        weather_city = (data['weather'][0]['main'])
        humidity = (data['main']['humidity'])

        # weatherbit website variables
        wind_dir = (data2['data'][0]['wind_cdir_full'])
        wind_spd = (data2['data'][0]['wind_spd'])
        weather_dsp = (data2['data'][0]['weather']['description'])

        # goweather website variables
        # day1 = (data3['forecast'][0])
        # day2 = (data3['forecast'][1])
        # day3 = (data3['forecast'][2])

        with open(f"team.txt", mode="a") as file:
            file.write("\n" + f'{dt_Kl.strftime("                                                          Date:-%d-%m-%y")}  '
                              f'\n{dt_Kl.strftime("                                                          Time:- %H:%M:%S")}  \nCity:- {city}')
            file.write("\n" + f"Weather looking like- {weather_city} ({weather_dsp}) \nMax.temp- {temp_max}°C \nMin.temp- {temp_min}°C "
                              f"\nHumidity- {humidity} % \nWind speed- {wind_spd} m/s  \nWind direction: {wind_dir} \n")
            file.write("--------------------------------------------------------------------")
        user_input()

    except KeyError:
        print("City not found")
    except requests.exceptions.SSLError:
        print("Please make sure you are connected to Internet or not...")
