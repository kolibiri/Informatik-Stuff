#Yet another database manager running on Mysql

#!usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from tkinter import *
from tkinter import messagebox


def reset():
    Server = "localhost"
    Benutzer = "root"
    Passwort = ""
    Datenbank = ""


def show_info(inp1):
     if messagebox.showinfo(inp1):
        main.destroy()


def save(e1, e2, e3, e4):
    try:
      Server = e1.get()
      Benutzer = e2.get()
      Passwort = e3.get()
      Datenbank = e4.get()

    except NameError():
        pass



#create config window
def create_window1():
    x = 0
    y= 0
    conf = Toplevel(main)
    conf.title("Einstellungen")
    en1 = Entry(conf)
    en2 = Entry(conf)
    en3 = Entry(conf)
    en4 = Entry(conf)
    enconf = [en1, en2, en3, en4]
    for e in enconf:
        e.grid(row=x, column=2)
        x+= 1

    l1=Label(conf,text="Server :")
    l2=Label(conf,text="Benutzername:")
    l3=Label(conf,text="Passwort:")
    l4=Label(conf,text="Datenbank:")
    labelsconf=[l1, l2, l3, l4]
    for l in labelsconf:
        l.grid(row=y)
        y += 1

    bconf = Button(conf, text="Standardwerte wiederherstellen", command=reset)
    bconf.grid(row=4, column = 5)
    conf.protocol("WM_DELETE_WINDOW", save(en1, en2, en3, en4))

def on_closing():
    if messagebox.askokcancel("Beenden", "Wollen sie das Programm beenden ? "):
        main.destroy()

main=Tk()
main.title("Yet Another Database Management Software V0.0.1")

#Set variables
#Server = "localhost"
#Benutzer = "root"
#Passwort = ""
#Datenbank = "buechershop"

#create standard view
b1=Button(text="Config",command=create_window1)
head = Label(text="Yet Another Database Management Software")
head.grid(row=0)
b1.grid(row=1, column=4)
b2=Button(text="Verbinden")
b2.grid(row=1, column = 3)




#handle closing event
main.protocol("WM_DELETE_WINDOW", on_closing)

#Mainloop
main.mainloop()
