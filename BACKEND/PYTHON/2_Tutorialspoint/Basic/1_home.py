# Python is a general-purpose 
# interpreted, 
# interactive, 
# object-oriented, and 
# high-level programming language

import tkinter as tk

root=tk.Tk()
button=tk.Button(root,text="Text Button")
button.pack()

radio=tk.RADIOBUTTON(root,text="Radio Button")
radio.pack()

root.mainloop()




global x
def outer():

    x = "outer x"

    def inner():
        # nonlocal x  # nonlocal statement more often than the global statement because can be useful in order
        # to change the state of closures and decorators
        x = "inner x"
        print(x)
    inner()
    print(x)


outer()
