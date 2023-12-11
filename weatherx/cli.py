import click
import requests
from geopy.geocoders import Nominatim


@click.command()
@click.argument("metric", required=True)
@click.option("--cityname", "-n", default=None, type=str, required=False, help="city name (country)")
@click.option("--latitude", "-lat", default=40.71, type=float, required=False, help="latitude (in degrees)")
@click.option("--longitude", "-lon", default=-74.01, type=float, required=False, help="longitude (in degrees)")
def cli(metric: str, cityname: str, latitude: float, longitude: float) -> None:
    geolocator = Nominatim(user_agent="MyApp")
    
    if cityname is not None: 
        location = geolocator.geocode(cityname)
        latitude, longitude = location.latitude, location.longitude
        
        coordinates = str(latitude) + ", " + str(longitude)
        location = geolocator.reverse(coordinates)
        address = location.raw['address']

        city = address.get('city', '')
        country = address.get('country', '')
        
        r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(location.latitude) + '&longitude=' + str(location.longitude) + '&current_weather=true')
    else:
        
        coordinates = str(latitude) + ", " + str(longitude)
        location = geolocator.reverse(coordinates)
        address = location.raw['address']

        city = address.get('city', '')
        country = address.get('country', '')
        
        r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude) + '&longitude=' + str(longitude) + '&current_weather=true')
    
    if r.status_code == 200:
        if metric in r.json()["current_weather"]:
            print(f"Current {metric} in {city}, {country} is {r.json()['current_weather'][metric]}")
        else:
            print("Metric not supported!")
    else:
        print("Open-Meteo is down!")

if __name__ == "__main__":
    cli()