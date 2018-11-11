#Yet another database manager running on Mysql

#!usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from tkinter import *
from tkinter import messagebox




"""
def reset():
    Server = "localhost"
    Benutzer = "root"
    Passwort = ""
    Datenbank = "buechershop"
"""


"""
def save(e1, e2, e3, e4):
    try:
      global Server
      Server = e1.get()
      global Benutzer
      Benutzer = e2.get()
      global Passwort
      Passwort = e3.get()
      global Datenbank
      Datenbank = e4.get()

    except NameError():
        pass

"""
"""
#create config window
def create_window1():
    x = 0
    y= 0
    conf = Toplevel(main)
    conf.title("Einstellungen")
    en1c = Entry(conf)
    en2c = Entry(conf)
    en3c = Entry(conf)
    en4c = Entry(conf)
    enconf = [en1c, en2c, en3c, en4c]
    for e in enconf:
       e.grid(row=x, column=2)
       x+= 1

    l1c=Label(conf,text="Server :")
    l2c=Label(conf,text="Benutzername:")
    l3c=Label(conf,text="Passwort:")
    l4c=Label(conf,text="Datenbank:")
    labelsconf=[l1c, l2c, l3c, l4c]
    for l in labelsconf:
        l.grid(row=y)
        y += 1

    bconf = Button(conf, text="Standardwerte wiederherstellen", command=reset)
    bconf.grid(row=4, column = 2)
    conf.protocol("WM_DELETE_WINDOW", save(en1c, en2c, en3c, en4c))
"""
def on_closing():
     if messagebox.askokcancel("Beenden", "Wollen sie das Programm beenden ? "):
        myc.disconnect()
        main.destroy()



def execute(exec):
    cursor = myc.cursor(dictionary = True)
    cursor.execute(exec)
    listbox = Listbox(main)
    listbox.grid(row=1, column= 1)
    row = cursor.fetchone()
    index = 1
    while(row != None):
       listbox.insert(index, row)
       row = cursor.fetchone()

    cursor.close



main=Tk()
main.title("Yet Another Database Management Software V1.0")

#Set variables
Server = "localhost"
Benutzer = "root"
Passwort = ""
Datenbank = "buechershop"


myc = mysql.connector.connect(host=Server)
myc.cmd_change_user(username = Benutzer)
myc.database = Datenbank

#create standard view
commandlabel = Label(main, text="SQL-Befehl")
commandlabel.grid(row = 0, column = 0)
commandtext = Entry(main)
commandtext.grid(row = 0, column = 1)
commandbutton = Button(main, text="Befehl ausführen",  command=lambda: execute(commandtext.get()))
commandbutton.grid(row=0, column=2)


#handle closing event
main.protocol("WM_DELETE_WINDOW", on_closing)

#Mainloop
main.mainloop()
