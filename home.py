from tkinter import *

class Home:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x800') # (width x height)
        self.root.resizable(False,False)
        self.root.mainloop()
if __name__ == '__main__':
    Home()