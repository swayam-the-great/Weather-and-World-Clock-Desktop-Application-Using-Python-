
from tkinter import *
import tkinter as tk
from PIL import  ImageTk, Image

from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime as dt
import requests
import pytz

root=Tk()
root.title("CLOCK :)")
canva_height=420
canva_wide=720

root.geometry(f"{canva_wide}x{canva_height}")


def weatherpy():
   # try:
   # Time ACCORDING TO CITY

   CITY = textfield.get()
   print(CITY)
   geolocator = Nominatim(user_agent="geoapiExercises")
   location = geolocator.geocode(CITY)
   obj = TimezoneFinder()
   result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

   # print(result)

   home = pytz.timezone(result)
   local_time = dt.now(home)
   current_time = local_time.strftime("%I:%M %p")
   clock.config(text=current_time)
   name.config(text="CURRENT WEATHER")

   #text transfer ka jugad
   BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
   API_KEY = "03cfd883dbc61c147bfc7cd90f9a0acb"
  # CITy

   def kelvin_to_celsius(kelvin):
       celsius = kelvin - 273.15
       fahrenheit = celsius * (9 / 5) + 32
       return celsius, fahrenheit

   url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
   response = requests.get(url).json()

   temp_kelvin = response['main']['temp']
   temp_celsius, temp_fahrenheit = kelvin_to_celsius(temp_kelvin)
   feels_like_kelvin = response['main']['feels_like']
   feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius(feels_like_kelvin)
   wind_speed = response['wind']['speed']
   humidity = response['main']['humidity']
   description = response['weather'][0]['description']
   # sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
   #sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

   print(f" temperature in {CITY}:{temp_celsius:.2f} °C or {temp_fahrenheit:.2f} °F")
   print(f" temperature in {CITY} feels like {feels_like_celsius:.2f} °C or {feels_like_fahrenheit:.2f} °F")
   print(f" Humidity in {CITY}:{humidity}%")
   print(f" wind speed  in {CITY}:{wind_speed}m/s")
   print(f" General weather  in {CITY}:{description}")
   #print(f" Sunrises in {CITY} at {sunrise_time} local time")
   #print(f" Sunsets  in {CITY} at {sunset_time}local time ")
   fahren=f"{temp_fahrenheit:.2f}°F"
   temperature = f"{temp_celsius:.2f}°C"
   #condition1= f" temperature in {CITY} feels like {feels_like_celsius:.2f} °C or {feels_like_fahrenheit:.2f} °F"
   humid= f"{humidity}%"
   wind=f"{wind_speed}m/s"
   condition1=f"Weather feels like:{description}"
   condition= f"{description}"
   # print(f" Sunrises in {CITY} at {sunrise_time} local time")
   # print(f" Sunsets  in {CITY} at {sunset_time}local time ")

   f.config(text=fahren)
   t.config(text=temperature)
   c.config(text=condition1)
   h.config(text=humid)
   w.config(text=wind)
   d.config(text=condition)
   p.config(text=f"{temp_kelvin}K")
#GUI

# WEATHER KA GUI
bg_image = Image.open("pink.PNG")
# TODO: Resize these background images
bg_image= bg_image.resize((760,450))
photo = ImageTk.PhotoImage(bg_image)
bglabel = Label(root,image=photo)
bglabel.place(x=0, y=0)




logo_image = Image.open("logo.png")
# TODO: Resize these logo images
logo_image = logo_image.resize((180,180))
logo_photo = ImageTk.PhotoImage(logo_image)
logolabel = Label(root,image=logo_photo ,background="pink")
logolabel.place(x=50, y=82)


searchimage = Image.open("Copy of search.png")
# TODO: Resize these logo images
searchimage = searchimage.resize((475,77))
search_photo = ImageTk.PhotoImage(searchimage)
searchlabel = Label(root,image=search_photo ,background="pink")
searchlabel.place(x=20, y=10)

textfield=tk. Entry(root, justify="left",width=15, font=("lucidda", 30, "bold"), bg="#404040", border=0,fg="white" )
textfield.place(x=70, y=27)
textfield. focus()


searchicon = Image.open("search_icon.png")
searchicon = searchicon.resize((45,45))
Search_icon=ImageTk.PhotoImage(searchicon)
myimage_icon=Button(image=Search_icon,command=weatherpy, borderwidth=0, cursor="hand2", bg="#404040")
myimage_icon.place(x=400, y=27)
#GET WHEATHER

#getweat=Button(text="get weather",command=getweather,font='lucidda 10 bold ',fg='yellow',background='DeepSkyBlue2')
#getweat.place(x=479,y=38)

boximage = Image.open("Copy of box.png")
# TODO: Resize these logo images
boximage = boximage.resize((475,77))
box_photo = ImageTk.PhotoImage(boximage)
boxlabel = Label(root,image=box_photo ,background="pink")
boxlabel.place(x=120, y=320)

#DOWM BLUE BOX

label1=Label(root, text="WIND", font=("Helvetica", 10, 'bold'), fg="white",bg="DeepSkyBlue2")
label1.place(x=180,y=333)
label2=Label (root, text= "HUMIDITY", font=("Helvetica", 10, 'bold'), fg="white", bg="DeepSkyBlue2")
label2.place(x=250, y=333)
label3=Label(root, text="DESCRIPTION", font=("Helvetica", 10, 'bold'), fg="white", bg="DeepSkyBlue2")
label3.place(x=350, y=333)
label4=Label(root, text="TEMPERATURE", font=("Helvetica", 10, 'bold'), fg="white", bg="DeepSkyBlue2")
label4.place(x=480, y=333)


#UP DEGEE CELSIUS WALA

t=Label( font=("arial", 50, "bold"), fg="#ee666d", bg="pink")
t.place(x=230, y=90)

c=Label(font=("arial", 20, 'bold'),bg="pink")
c.place(x=230, y=225)
f=Label(font=("arial", 20, 'bold'),bg="pink")
f.place(x=230, y=190)

# PARAMETER ANSWERS

w=Label( font=("arial",15, "bold"), bg="DeepSkyBlue2")
w.place(x=174, y=350)
h=Label( font=("arial", 15, "bold"), bg="DeepSkyBlue2")
h.place(x=270, y=350)
d=Label( font=("arial", 15, "bold"), bg="DeepSkyBlue2")
d.place(x=373, y=350)
p=Label( font=("arial", 15, "bold"), bg="DeepSkyBlue2")
p.place(x=502, y=350)



#ALARM CLOCK GUI



#time CURRENT TIME

name=Label (root, font=("arial", 15, "bold"),bg="pink",fg="black")
name.place(x=500,y=60)
clock=Label(root, font=("Helvetica", 15),bg="pink",fg="black")
clock.place(x=500,y=85)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# LOGICS PART

# WEATHER











'''''''''

search=PhotoImage(file="Copy of search.png")
searchimg=Label(image=search ,background="pink")
searchimg.pack()
'''''''''

mainloop()

