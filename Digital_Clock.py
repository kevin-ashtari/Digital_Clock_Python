from tkinter import *
from time import *

def update():
    Time_string = strftime("%I:%M:%S %p")
    Time_label.config(text=Time_string)

    Day_string = strftime("%A")
    Day_label.config(text=Day_string)  

    Date_string = strftime("%B %d, %Y")
    Date_label.config(text=Date_string)  

# update every second or 100ms
    Window.after(1000,update)
    

Window = Tk()
# window font-size and color
Time_label = Label(Window,font=("Arial",50),fg="green",bg="black")
Time_label.pack()

Day_label = Label(Window,font=("Ink Free",25))
Day_label.pack()

Date_label = Label(Window,font=("Ink Free",30))
Date_label.pack()

update()

Window.mainloop()