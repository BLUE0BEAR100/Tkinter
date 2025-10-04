#Import tkinter
from tkinter import *
from datetime import date

#create window
window=Tk()

#set the tittle and geometry
window.title('First Window')
window.geometry('400x300')


#add wid
#add lbl
lbl=Label(text="Please fill the input box",fg="#FBC02D",bg="black",height=1,width=300)

#add label for getting name as input from user
#use entry widget to create text box for user to enter det
name_lbl=Label(text="Full name",bg="white")
name_entry=Entry()
name_entry.insert(0,"Enter your name")
#fucntion to display a msg
def display():
    #read input given by user
    name = name_entry.get()

    #declaring a global var
    #to make it accessible anywhere in the program
    global message
    message="Welcome to the application!  \nToday's date is: "
    greet="Hello "+name+'\n'

    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
#add a text widget to display info/msg
text_box=Text(height=3)
#add btn and give value of command as name of the func
#press button display fucntion will be called automatically
btn=Button(text="Begin",command=display,height=1,bg="black",fg="#FBC02D")

#organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()