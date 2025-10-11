#Import tkinter
from tkinter import*

#create window
window=Tk()
window.title("Length Converter")
window.geometry('400x400')

#Create Frame
frame=Frame(master=window,height=200,width=400)
#add wid
#add lbl
lbl1=Label(frame,text="Num 4 Converted ",bg="gray",fg='white',width=14)
#use entry wid 
Length_entry=Entry(frame)

def display():
    Length=float(Length_entry.get())
    GivenNum="Hey your number converting to cm "
    result =100 * Length
    textbox.insert(END,GivenNum)
    textbox.insert(END,result)
textbox=Text(bg="gray",fg="black")

btn=Button(text="Convert ! ",command=display,bg="red")


frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
Length_entry.place(x=150,y=20)
btn.place(x=140,y=60)
textbox.place(y=100)

window.mainloop()