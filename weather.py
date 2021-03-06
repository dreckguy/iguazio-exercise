# importing requests and json
import sys,requests, json
API_KEY = sys.argv[1]
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Tel-Aviv"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   print( CITY + ':')
   print('Temperature: ' + str(temperature))
   print('Humidity: ' + str(humidity))
   print('Pressure: ' + str(pressure))
   print('Weather Report: ' + report[0]['description'])
else:
   # showing the error message
   print("Error in the HTTP request")