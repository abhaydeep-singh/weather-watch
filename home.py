from tkinter import *
import ctypes
class Home:
   
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x800') # (width x height)
        self.root.title("Weather Watch")
        self.root.resizable(False,False)
        self.frame=Frame(self.root,bg='#333333')
        self.frame.place(x=0, y=0, height=800, width=800)

        self.btn2 = Button(self.frame,text= 'Change',bg='#333333', fg='white', command=self.change_wallpaper)
        self.btn2.place(x=300, y=300, height= 30, width= 150)


        self.root.mainloop()

    def change_wallpaper(self):
        SPI_SETDESKWALLPAPER = 20
        path = "G:\Python\Projects\images\wallpaper.jpg"
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

            # if __name__ == "__main__":
            #     path = "G:\Python\Projects\images\wallpaper.jpg"
            #     change_wallpaper(path)


if __name__ == '__main__':
    Home()


   

