from tkinter import *
from tkinter import messagebox
import home
class Page1:
    themeColor = 'yellow'
    userName = 'abhay'
    passWord = 'singh'
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x800') # (width x height)
        self.root.resizable(False,False)
        self.frame=Frame(self.root,bg='#333333')
        self.frame.place(x=0, y=0, height=800, width=800)
        

        self.label1 = Label(self.frame, text='Username',bg='#333333', fg= self.themeColor, font=('Arial',18), anchor="w")
        self.label1.place(x=300, y=300, height=30, width=200)

        self.entry1 = Entry(self.frame,bg='#333333',fg='white', borderwidth = 2, relief = "groove")
        self.entry1.place(x=300, y=330, height=30, width=200)

        self.label2 = Label(self.frame, text='Password',bg='#333333', fg= self.themeColor, font=('Arial',18,), anchor="w")
        self.label2.place(x=300, y=380, height=30, width=200)

        self.entry2 = Entry(self.frame, bg='#333333',fg ='white',show="*", borderwidth = 2, relief = "groove")
        self.entry2.place(x=300, y=410, height=30, width=200)

        self.btn1=Button(self.frame,text = 'Submit', bg= self.themeColor, fg='Black', font=('Arial',15), command = self.onClick)
        self.btn1.place(x=300, y=480, height= 40, width= 200)
        self.root.mainloop()

    # method to get data from two entries
    def onClick(self):
        a = self.entry1.get()
        b = self.entry2.get()

        if a == self.userName and b == self.passWord:
           
            # page routing
            self.root.destroy()
            home.Home()
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        elif a == '' or b == '':
            messagebox.showwarning(title="Warning", message="Do not leave any space empty")
        else:
            messagebox.showerror(title="Error", message="Invalid login.")



        
   


        
if __name__ == '__main__':
    Page1()