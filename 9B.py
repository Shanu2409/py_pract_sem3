from tkinter import *

root = Tk()
root.geometry("300x300")
var = IntVar()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

Button1 = Checkbutton(root, text="Tutorial", variable=Checkbutton1,
                      onvalue=1, offvalue=0, height=2, width=10)

Button2 = Checkbutton(root, text="Student", variable=Checkbutton2,
                      onvalue=1, offvalue=0, height=2, width=10)

Button3 = Checkbutton(root, text="Courses", variable=Checkbutton3,
                      onvalue=1, offvalue=0, height=2, width=10)

Button1.pack()
Button2.pack()
Button3.pack()

R2 = Radiobutton(root, text="Option 2", variable=var, value=3)
R2.pack(anchor=CENTER)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3)
R3.pack(anchor=CENTER)

scale = Scale(root, variable=var)
scale.pack(anchor=CENTER)
label = Label(root)
label.pack()

mainloop()
