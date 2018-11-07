from tkinter import *

def an():
    label.config(bg= "white", fg = "black", text="An")

def aus():
    label.config(bg="black", fg = "white",text="Aus")

main = Tk()
main.title("Lichtschalter")
label = Label(text="Aus", bg = "black", fg = "white", pady= 30, padx= 40)
b1=Button(main, text="An", command=an, padx= 20)
b2=Button(main, text="Aus", command=aus, padx= 20)


label.pack(pady=10, expand=1)
b1.pack(anchor= "s",expand=1)
b2.pack(anchor= "s", expand=1)
main.mainloop()