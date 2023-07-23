from tkinter import *
import ctypes # it is for changing desktop wallpaper 
import requests
from PIL import Image, ImageTk
# import login
class Home:
    API_KEY = "ce42a8b45d885f469ac82d490100d6a2"
    API_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self):

        

        self.root = Tk()
        self.root.geometry('800x800') # (width x height)
        self.root.title("Weather Watch")
        self.root.resizable(False,False)

        self.frame1=Frame(self.root,bg='#333333')
        self.frame1.place(x=0, y=0, height=800, width=800)

        self.frame2=Frame(self.root,bg='#292929')
        self.frame2.place(x=0, y=0, height=200, width=800)

        self.frame3=Frame(self.root,bg='#2e2e2e')
        self.frame3.place(x=480, y=260, height=240, width=290)

        # inserting logo1
        self.logo1=Image.open('G:\Python\Projects\images\weather.png').resize((120,120)) #opening and resizing image
        self.logoImage=ImageTk.PhotoImage(self.logo1)
        self.label=Label(self.frame2, image=self.logoImage, bg='#292929')
        self.label.place(x=60, y=40, width=120,height=120)
        #title
        self.textLabel = Label(self.frame2, text='Weather Watch', bg='#292929', fg= 'yellow', font=('Arial',60), anchor="w")
        self.textLabel.place(x=200, y=60, height=75, width=570)


        # self.btn2 = Button(self.frame,text= 'Change',bg='#333333', fg='white', command=self.change_wallpaper)
        # self.btn2.place(x=300, y=300, height= 30, width= 150)

        # city label
        self.city_label = Label(self.root, text='Enter city here: ', bg='#2e2e2e', fg='yellow', font=('Arial',17))
        self.city_label.place(x=510, y=315, height= 30, width= 230)

        # city entry
        self.city_entry = Entry(self.root,fg='white', bg='#2e2e2e',font=(10), borderwidth = 2, relief = "groove")
        self.city_entry.place(x=510, y=350, height=30, width = 230)

        # Weather_Label_Text
        self.weather_label_text = Label(self.frame1, text = "Weather",bg='#333333',fg='yellow', font=('Arial',20), anchor='w')
        self.weather_label_text.place(x=90, y=280, height=40, width= 130)
        # Weather_Label
        self.weather_label = Label(self.frame1, text = "", font=('Arial',18),bg='#333333',fg='white', anchor='w')
        self.weather_label.place(x=280, y=280, height=40, width= 180)

        # temperature_Label_Text
        self.temperature_label_text = Label(self.frame1, text = "Temperature",bg='#333333',fg='yellow', font=('Arial',20), anchor='w')
        self.temperature_label_text.place(x=90, y=350, height=40, width= 180)

        # Temperature_Label
        self.temperature_label = Label(self.frame1, text = "", font=('Arial',18),bg='#333333',fg='white', anchor='w')
        self.temperature_label.place(x=280, y=350, height=40, width= 150)

        # humidity_Label_Text
        self.humidity_label_text = Label(self.frame1, text = "Humidity",bg='#333333',fg='yellow', font=('Arial',20), anchor='w')
        self.humidity_label_text.place(x=90, y=420, height=40, width= 150)

        # Humidity_Label
        self.humidity_label = Label(self.frame1, text = "", font=('Arial',18),bg='#333333',fg='white', anchor='w')
        self.humidity_label.place(x=280, y=420, height=40, width= 150)


        # Get weather button
        self.get_weather_button = Button(self.root, text="Get Weather", bg= 'yellow', fg='Black', font=('Arial',15), command = self.get_weather)
        self.get_weather_button.place(x=510, y=400, height=30, width= 230)


        self.root.mainloop()


    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            self.weather_label.config(text="Please enter a city.")
            return

        params = {
            "q": city,
            "appid": self.API_KEY,
            "units": "metric"  # Change to "imperial" for Fahrenheit
        }

        try:
            response = requests.get(self.API_URL, params=params)
            data = response.json()
            if data["cod"] == 200:
                # creating variables
                weatherInfo = data['weather'][0]['description']
                temperatureInfo = (data['main']['temp'], '°C')
                humidityInfo = (data['main']['humidity'], '%')

                # weather_info = f"Weather: {weatherInfo}\nTemperature: {temperatureInfo}°C\nHumidity: {humidityInfo}%"
                self.weather_label.config(text=weatherInfo)
                self.temperature_label.config(text=temperatureInfo)
                self.humidity_label.config(text=humidityInfo)
            else:
                self.weather_label.config(text=f"Error: {data['message']}")
        except requests.exceptions.RequestException:
            self.weather_label.config(text="Error: Connection Error")


   


if __name__ == '__main__':
    Home()


   



























 # # method to change desktop wallpaper
    # def change_wallpaper(self):
    #     SPI_SETDESKWALLPAPER = 20
    #     path = "G:\Python\Projects\images\pic.jpg"
    #     ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
