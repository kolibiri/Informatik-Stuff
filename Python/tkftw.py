from tkinter import *

def changeb1():
    b1.config(text="Such wow\n Much amazing", font =("Comic Sans MS",20))
    titel.config(fg='blue', bg='yellow')

window = Tk()
window.title("( ͡° ͜ʖ ͡°)")
fr1 = Frame(relief=RIDGE, bd=2)
titel = Label(window, text='IKEA', fg='red',font=("Comic Sans MS",20))
b1 = Button(fr1, text="Klick mich", command=changeb1, pady= 100, padx= 100)
label = [Label(window, font=('Arial',40), text='riesig', width=10),
Label(window, font=('Arial',20), text='mittel'),
Label(window, font=('Comic Sans MS',5), text='Wer das liest ist dumm')]

en1 = Entry()

#for l in label:
    #l.pack(pady = 50)
fr1.pack(side=BOTTOM,expand=1)
en1.pack(expand=1)
s = en1.get()
titel.pack()
b1.pack(pady = 50, padx = 30)
window.mainloop()