import datetime
import requests

class Song:
    def __init__(self, name, weather, hour):
        self.name = name
        self.weather = weather
        self.hour = hour

def getWeather():
    API_URL = "http://api.openweathermap.org/data/2.5/weather?lat="
    KEY = "4bc8eb78acd942d6594974295c615f5f"

    #coordinates for Olympia, WA
    latitude = "47.0379"
    longitude = "122.9007"

    #final url (end point)
    url = API_URL + latitude + "&lon=" + longitude + "&appid=" + KEY

    response = requests.get(url).json()
    #parse json
    weather = response['weather'][0]['main']
    return weather

#get song name, hour, and weather
songName = input("What is the name of the song?")
currentTime = datetime.datetime.now()
currentHour = str(currentTime.hour) 
#currentHour = str(currentHour)
weather = getWeather()

#test
#print(songName, weather, currentHour)

#appends song to file
file = open("C:\\Users\\griff\\Documents\\SongsWeatherTime.txt", "a")
file.write(songName + ", " + currentHour + ", " + weather + "\n")
file.close()


#convert from military time

#read from file and make an array songs
fileRead = open("C:\\Users\\griff\\Documents\\SongsWeatherTime.txt", "r")
lines = fileRead.readlines()
for line in lines:
    if (line.find(songName) != -1):
        print(line)
        







    
