import requests
import sys
""" Creator of petitions to OpenWeather

This module allows the user to create a petition to Open Weather
and to get the weather of a city using its coordenates
This tool requires an stable internet conection
This module contains the following functions:
   * create(lat:str,long_str) - returns the weather of the city
"""
api_key = "3197eecbf35d14338c5f1703d18dbb0e"

def create(lat, lon):
    """ Gets the city's weather
    Parameters
    ----------
    lat : str
       the latitude of the city
    long : str
       the longitude of the city
    Returns
    -------
    weather : str
      The city's weather
    """
    
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid={}".format(lat,lon, api_key)
        request = requests.get(url)
        dictionary = request.json()
    except:
        sys.exit("An error ocurred comunicating with the server")

    if(dictionary.get("cod") == "400"):
        return "Invalid city"

    weather = "The city {} has a weather ".format(dictionary.get("name"))
    # in the JSON dictionary['weather'] is a list, with a string, down is splitted
    weather += str(dictionary.get('weather')).split("main")[1].split("\'")[2] 
    weather += " and a temperature of {}°C".format(dictionary.get("main",{}).get("temp")) 
    return weather
    
