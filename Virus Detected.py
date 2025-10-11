#import necessary libraries
from tkinter import*
from tkinter import messagebox

#set up tkinter window
window=Tk()
window.geometry("200x200")

#Fucntion for displaying warning message
#This will be called once the button is clicked
#massagebox.showwarning("Window Name","Text to be displayed")
def msg():
    messagebox.showwarning("Alert","Stop! Virus Found.")

#adding button widget to window
button=Button(window,text="Scan for virus",command=msg)
button.place(x=40,y=80)

#entering main event loop
window.mainloop()