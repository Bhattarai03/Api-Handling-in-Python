import requests
def fetch_city_long_lat(city):
    try:
        url_city=(
            f"http://api.openweathermap.org/geo/1.0/direct"
            f"?q={city}&limit=1&appid=cffbc7f3f3dd6fb43b36b322673f096a"
        )
        response=requests.get(url_city)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
         raise Exception(f"Request failed: {e}")
        
    content=response.json()
    if  content :
        latitude=content[0]["lat"]
        longitude=content[0]["lon"]
        return latitude,longitude
    else:
        raise Exception ("Failed to fetch the data")
def fetch_weather_data(namecity):
    latitude,longitude=fetch_city_long_lat(f"{namecity}")
    try:
        url=(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=cffbc7f3f3dd6fb43b36b322673f096a&units=metric")
        response1=requests.get(url)
        response1.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
    data=response1.json()
    if  data["cod"]==200 :
        weather=data["weather"][0]["description"]
        temperature=data["main"]["temp"]
        pressure=data["main"]["pressure"]
        windspeed=data["wind"]["speed"]
        timezone=data["timezone"]
        Sunrise=data["sys"]["sunrise"]
        Sunset=data["sys"]["sunset"]
        return weather,temperature,pressure,windspeed,timezone,Sunrise,Sunset
    else:
        raise Exception ("Failed to fetch the weather data")
def main():
    cityname=(input("Enter the city you wanted to check the weather :"))
    try:
        weather,temperature,presssure,windspeed,timezone,sunrise,sunset=fetch_weather_data(f"{cityname}")
        print(f"Weather : {weather}  \n Temperature :{temperature} \n Pressure :{presssure} \n Timezone :{timezone} \n Sunrise:{sunrise} \n Sunset :{sunset}")
    except Exception as ee:
        print(str(ee))
if __name__=="__main__":
    main()


    


