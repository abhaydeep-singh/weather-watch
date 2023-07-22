from tkinter import *
import ctypes # it is for changing desktop wallpaper 
import requests
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

        # self.btn2 = Button(self.frame,text= 'Change',bg='#333333', fg='white', command=self.change_wallpaper)
        # self.btn2.place(x=300, y=300, height= 30, width= 150)

        # city label
        self.city_label = Label(self.frame1, text='Enter city here: ')
        self.city_label.place(x=100, y=100, height= 30, width= 150)
        # city entry
        self.city_entry = Entry(self.frame1)
        self.city_entry.place(x=100, y=140, height=30, width = 150)

        # Weather_Label
        self.weather_label = Label(self.frame1, text = "")
        self.weather_label.place(x=200, y=200, height=70, width= 200)

        # creating button
        self.get_weather_button = Button(self.frame1, text="Get Weather", command=self.get_weather)
        self.get_weather_button.place(x=200, y=400, height=20, width= 200)


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
                weather_info = f"Weather: {data['weather'][0]['description']}\nTemperature: {data['main']['temp']}°C\nHumidity: {data['main']['humidity']}%"
                self.weather_label.config(text=weather_info)
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
