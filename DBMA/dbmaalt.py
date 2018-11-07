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


#ask user for verification of exiting and close everything
def on_closing():
    if messagebox.askokcancel("Beenden", "Wollen sie das Programm beenden ? "):
        myc.disconnect()
        main.destroy()


def create_window():
    real = Toplevel()
    real.title("DBMA V0.0.2")
    head = Label(real, text="Yet Another Database Management Software")
    real.focus_set()
    head.grid(row=0)
    b2=Button(real, text="Verbinden")
    b2.grid(row=1, column = 3)




main=Tk()
main.title("Einstellung der Verbindung")

#loop variables
x = 0
y = 0

#Set standard variables
Server = "localhost"
Benutzer = "root"
Passwort = ""
Datenbank = "buechershop"

en1 = Entry(main)
en2 = Entry(main)
en3 = Entry(main)
en4 = Entry(main)
enconf = [en1, en2, en3, en4]
for e in enconf:
    e.grid(row=x, column=2)
    x+= 1

l1=Label(main,text="Server :")
l2=Label(main,text="Benutzername:")
l3=Label(main,text="Passwort:")
l4=Label(main,text="Datenbank:")
labelsconf=[l1, l2, l3, l4]
for l in labelsconf:
    l.grid(row=y)
    y += 1

bconf = Button(main, text="Standardwerte wiederherstellen", command=reset)
bconf.grid(row=4, column = 2)
blaunch = Button(text="Starte das Programm", command=create_window())
blaunch.grid(row=4, column=0)



#handle closing event
#main.protocol("WM_DELETE_WINDOW", on_closing)

#Mainloop
main.mainloop()
