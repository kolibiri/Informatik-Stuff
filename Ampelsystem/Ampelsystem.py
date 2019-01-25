from tkinter import *
from time import sleep
from time import *
from threading import *

class Auto_Ampel(object):
    def __init__(self):
        self.lampeRot = False
        self.lampeGelb = False
        self.lampeGruen = False
        self.status = "aus"
        self.exc=0
        self.frame = Frame(main, background="black")
        self.blackcanvas1 = Canvas(self.frame, width=50, height=50, bg="black")
        self.blackcanvas2 = Canvas(self.frame, width=50, height=50, bg="black")
        self.blackcanvas3 = Canvas(self.frame, width=50, height=50, bg="black")
        self.blackcanvas1.grid(row=0, column=0)
        self.blackcanvas2.grid(row=1, column=0)
        self.blackcanvas3.grid(row=2, column=0)

    def set_Lampen(self, startwertLampeRot, startwertLampeGelb, startwertLampeGruen):
        self.lampeRot = startwertLampeRot
        self.lampeGelb = startwertLampeGelb
        self.lampeGruen = startwertLampeGruen



    def schalten(self):
        if (self.lampeRot, self.lampeGelb, self.lampeGruen) == (True, False, False):
            self.set_Lampen(True, True, False)
            self.status = "rotgelb"

        elif(self.lampeRot, self.lampeGelb, self.lampeGruen) == (True, True, False):
            self.set_Lampen(False, False, True)
            self.status = "gruen"

        elif(self.lampeRot, self.lampeGelb, self.lampeGruen) == (False, False, True):
            self.set_Lampen(False, True, False)
            self.status = "gelb"


        elif(self.lampeRot, self.lampeGelb, self.lampeGruen) == (False, True, False):
            self.set_Lampen(True, False, False)
            self.status = "rot"

        self.update()

#TODO : test mode

    def testmodus(self):
        self.test = 1
        self.lampeRot = False
        self.lampeGelb = False
        self.lampeGruen = False
        self.status = "aus"
        self.update()


        while(self.test == 1):
            self.lampeGelb = True
            self.status="gelb"
            self.update()
            sleep(1.5)
            self.lampeGelb = False
            self.status = "aus"
            self.update()

    def initialize_normal(self):
        self.lampeRot = True
        self.lampeGelb = False
        self.lampeGruen = False
        self.status = "rot"
        self.update()

    def update(self):
        if(self.status=="rotgelb"):
            self.yellow = self.blackcanvas2.create_oval(1, 1, 50, 50, fill="yellow")

        elif(self.status=="gruen"):
            self.blackcanvas1.delete(self.red)
            self.blackcanvas2.delete(self.yellow)
            self.green = self.blackcanvas3.create_oval(1, 1, 50, 50, fill="green")

        elif(self.status=="gelb"):
            self.blackcanvas3.delete(self.green)
            self.yellow = self.blackcanvas2.create_oval(1, 1, 50, 50, fill="yellow")
            self.exc=1

        elif(self.status=="rot"):
            self.blackcanvas2.delete(self.yellow)
            self.red = self.blackcanvas1.create_oval(1, 1, 50, 50, fill="red")

        elif(self.status == "aus"):
            try:
                self.reset()

            except Exception:
                pass



    def set_location(self, x, y):
        self.frame.grid(row=x, column=y)


    def initialize(self, x, y, status):
        if(status=="rot"):
            self.set_Lampen(True, False, False)
            self.status = status
            self.red = self.blackcanvas1.create_oval(1, 1, 50, 50, fill="red")

        elif(status=="gruen"):
            self.set_Lampen(False, False, True)
            self.status = status
            self.green = self.blackcanvas3.create_oval(1, 1, 50, 50, fill="green")

        elif(status=="gelb"):
            self.set_Lampen(False, True, False)
            self.status = status
            self.yellow = self.blackcanvas2.create_oval(1, 1, 50, 50, fill="yellow")

        elif(status=="rotgelb"):
            self.set_Lampen(True, True, False)
            self.status = status
            self.red = self.blackcanvas1.create_oval(1, 1, 50, 50, fill="red")
            self.yellow = self.blackcanvas2.create_oval(1, 1, 50, 50, fill="yellow")

        self.set_location(x, y)

        def reset(self):
            try:
              self.blackcanvas1.delete(self.red)
              self.blackcanvas2.delete(self.yellow)
              self.blackcanvas3.delete(self.green)

            except Exception:
                pass


class andere_ampel(object):
    def __init__(self):
        self.green = False
        self.red = True
        self.frame = Frame(main, background="black")
        self.blackcanvas1 = Canvas(self.frame, width=30, height=30, bg="black")
        self.blackcanvas2 = Canvas(self.frame, width=30, height=30, bg="black")
        self.status = "aus"
        self.blackcanvas1.grid(row=0, column=0)
        self.blackcanvas2.grid(row=1, column=0)

    def set_Lampen(self, startwertLampeRot, startwertLampeGruen):
        self.lampeRot = startwertLampeRot
        self.lampeGruen = startwertLampeGruen

    def reset(self):
        try:
            self.blackcanvas1.delete(self.red)
            self.blackcanvas2.delete(self.green)

        except Exception:
            pass



    def set_location(self, x, y):
        self.frame.grid(row=x, column=y)

        self.update()

    def initialize(self, x, y, status):
        if(status=="rot"):
            self.set_Lampen(True, False)
            self.status = status

        elif(status=="gruen"):
            self.set_Lampen(False, True)
            self.status = status

        self.update()
        self.set_location(x, y)


    def update(self):
        if (self.status == "rot"):
            self.reset()
            self.red = self.blackcanvas1.create_oval(1, 1, 30, 30, fill="red")

        elif(self.status == "gruen"):
            self.reset()
            self.green = self.blackcanvas2.create_oval(1, 1, 30, 30, fill="green")


    def schalten(self):
        if(self.status=="rot"):
            self.set_Lampen(False, True)
            self.status = "gruen"

        elif(self.status=="gruen"):
            self.set_Lampen(True, False)
            self.status = "rot"

        self.update()








def alle_schalten(dest):
    x = 0
    while(x < len(dest)):
        dest[x].schalten()
        x += 1




def add_to_object_array(obj, dest):
    dest.append(obj)

#TODO : Automatic switching


def auto():
    sleep(5)
    for o in object_array:
        if(o.status == "gruen"):
            o.schalten()

    sleep(0.5)
    for o in object_array:
        if(o.status == "gelb"):
            o.schalten()

    for f in fuß_array:
        if(f.status == "gruen"):
            f.schalten()

    sleep(3)
    for o in object_array2:
        if(o.status=="rot"):
            o.schalten()

    sleep(1)
    for o in object_array2:
       if(o.status=="rotgelb"):
           o.schalten()

    fuß_array[0].schalten()
    sleep(5)

    for o in object_array2:
        if(o.status=="gruen"):
            o.schalten()

    sleep(1)
    for o in object_array2:
        if(o.status=="gelb"):
            o.schalten()
    sleep(5)
    for o in object_array:
        if(o.status=="rot"):
            o.schalten()
    sleep(1)
    fuß_array[0].schalten()

    for o in object_array:
        if(o.status=="rotgelb"):
            o.schalten()







def start_auto():
    Ampel1 = Auto_Ampel()
    Ampel1.initialize(0, 0, "rot")
    add_to_object_array(Ampel1, object_array2)

    Ampel2 = Auto_Ampel()
    Ampel2.initialize(1, 0, "gruen")
    add_to_object_array(Ampel2, object_array)

    Ampel3 = Auto_Ampel()
    Ampel3.initialize(0, 3, "rot")
    add_to_object_array(Ampel3, object_array2)

    Ampel4 = Auto_Ampel()
    Ampel4.initialize(1, 3, "gruen")
    add_to_object_array(Ampel4, object_array)

    fuß1 = andere_ampel()
    fuß1.initialize(0, 4, "rot")
    add_to_object_array(fuß1, fuß_array)

    fuß2 = andere_ampel()
    fuß2.initialize(1, 4, "gruen")
    add_to_object_array(fuß2, fuß_array)

    while(True):
       auto()



def stoptest():
    stop = True




main = Tk()
main.title("Ampelschaltung")
main.geometry("480x360")
main.iconbitmap("Ampelicon.ico")

object_array = []
object_array2 = []
fuß_array = []
stop = False

debugbutton = Button(main, text="Schalten", command=lambda: alle_schalten(object_array))
debugbutton.grid(row=0, column=2)
debug2button = Button(main, text="Fussgänger Schalten", command=lambda: alle_schalten(fuß_array))
debug2button.grid(row=1, column=2)
loop = Thread(target=start_auto)
loop.start()

main.mainloop()
