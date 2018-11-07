#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jonas.bremer
#
# Created:     15.10.2018
# Copyright:   (c) jonas.bremer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!usr/bin/env python
# -*- coding: utf-8 -*-


import mysql.connector


Server = "localhost" #or localhost var
Benutzer = "root"   # set username var
#Passwort = "phpadmin"  # set password var
Database = "buechershop" # set database var

myc = mysql.connector.connect(host=Server) # connect to Server
myc.cmd_change_user(username = Benutzer)   #login
myc.database = Database   # connect to databse
#print("You are now connected")  # debug

cursor = myc.cursor(dictionary = True) #create cursor
exec = "SELECT * FROM buecher"
cursor.execute(exec)
row = cursor.fetchone()

while(row != None):
    print(row["Titel"], row ["Preis"])
    row = cursor.fetchone()

cursor.close() # end cursor
myc.disconnect() #ciao






