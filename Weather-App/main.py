import requests
import json
import win32com.client as wincom

city = input("Enter the city name: ")
url = f"http://api.weatherapi.com/v1/current.json?key=df6ca3c54d1d4621aa1181017251808&q={city}"

response = requests.get(url)

# Convert API response to dictionary
wdic = response.json()  # no need to load again with json.loads

print(wdic['current']['temp_c'])  # Print the current temperature in Celsius    

speak = wincom.Dispatch("SAPI.SpVoice")

text = f"The current temperature in {city} is {wdic['current']['temp_c']} degrees Celsius."
speak.Speak(text)
