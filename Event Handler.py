#Import Tkinter
from tkinter import*
#Create window
window=Tk()
window.title("Event Handler")
window.geometry("100x100")

#Event Handler for keypress
def handel_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

#Blind keypress event to handle_Keypress()
window.bind("<Key>",handel_keypress)

#Event handler for button click
def handle_click(event):
    print("\nButton was clicked")

button=Button(text="Click Me!")
button.pack()

#bind click event to handle click
button.bind("<Button-1>",handle_click)

#start the gui event loop
window.mainloop()