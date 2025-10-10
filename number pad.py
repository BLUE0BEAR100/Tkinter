#import tkinter
from tkinter import*

#create window
window=Tk()
window.title('Number Pad')
window.geometry('250x300')

#create a frame to organize elements better
frame=Frame(master=window,height=200,width=360,bg="#d0efff")

nums = [[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]

for i in range(4):
    #configure rows and columns to resize window
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        frame=Frame(
            master=window,
            relief=SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i,column=j)
        label=Label(master=frame,text=nums[i][j],
bg='#D0efff')
        label.pack(padx=3,pady=3)

#Start the GUI event loop
window.mainloop()