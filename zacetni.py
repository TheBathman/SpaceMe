from tkinter import *


root = Tk()
root.title("SpaceMe")

#Izberi nacin igre:
Label(root, text="Select players:").grid(row=1, column=0, padx=50)
#pack(padx=5, pady=0)

v = IntVar()

Radiobutton(root, text="P v P", padx = 20, variable=v, value=1).grid(row=2, column=0, padx=50, pady=5)
Radiobutton(root, text="P v C", padx = 20, variable=v, value=2).grid(row=3, column=0, padx=50, pady=5)
Radiobutton(root, text="C v P", padx = 20, variable=v, value=3).grid(row=4, column=0, padx=50, pady=5)
Radiobutton(root, text="C v C", padx = 20, variable=v, value=4).grid(row=5, column=0, padx=50, pady=5)

#Izberi velikost polja:
Label(root, text="Choose field size:").grid(row=1, column=5, padx=50, pady=5)

slide = Scale(root, from_=5, to=20, orient=HORIZONTAL).grid(row=2, column=5, padx=50)

Button(root, text='Start').grid(row=4, column=5)
Button(root, text='Help').grid(row=5, column=5)


mainloop()