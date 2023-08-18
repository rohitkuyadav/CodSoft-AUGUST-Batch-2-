# importing module

import requests
"""
The requests module allows you to send HTTP requests using Python. 
The HTTP request returns a Response Object with all the response data (content, encoding, status, etc)
"""
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import *

# API key 
def api_key():
    return "a31ffdd66fa05a9f408cf12067274ac3" 

# Create GUI window
main = tk.Tk()
main.title("Weather Forcast Application")
main.geometry("400x250")

# Setting icon of master window
p1 = PhotoImage(file = 'cloudy.png')
main.iconphoto(False, p1)

# Add labels and entry box
city_label = tk.Label(main, text="Enter city Name")
city_label.pack()
city_entry = tk.Entry(main)
city_entry.pack()
weather_label = tk.Label(main, text="")
weather_label.pack()

# Fetch weather data and update GUI
def get_weather():
    city_name = city_entry.get()
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key() + "&q=" + city_name
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        y = data["main"]
        current_temperature = y["temp"]
        current_humidity = y["humidity"]
        z = data["weather"]
        celsius = "°C"
        weather_description = z[0]["description"]
        
        result = f"Temperature: {current_temperature-273.15, celsius}\nHumidity: {current_humidity}\nConditions: {weather_description}"
        weather_label["text"] = result
        
    else:
        weather_label["text"] = "City not found"
        
# Button to trigger API call        
search_btn = tk.Button(main, text="Search Weather", command=get_weather)
search_btn.pack()
main.mainloop()
