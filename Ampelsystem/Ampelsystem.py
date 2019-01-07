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

    def stoptest(self):
        self.test = 0
        sleep(1)
        self.initialize_normal()


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
            if(self.exc==1):
                self.blackcanvas2.delete(self.yellow)

            self.red = self.blackcanvas1.create_oval(1, 1, 50, 50, fill="red")

        elif(self.status == "aus"):
            self.blackcanvas1.delete(self.red)




    def start_auto(self):
        self.loop = Thread(target=auto())
        self.loop.start()


    def set_location(self, x, y):
        self.frame.grid(row=x, column=y)




    def auto(self):
        pass


    def initialize(self, x, y):
        self.initialize_normal()
        self.set_location(x, y)
        add_to_global_index()




def alle_schalten():
    pass

def add_to_global_index():
    pass


main = Tk()
main.title("Ampelschaltung")
main.geometry("480x360")

"""greencanvas = Canvas(main, width=50, height=50, bg="black")
green = greencanvas.create_oval(1, 1, 50, 50, fill="green")
greencanvas.grid(row=0, column=0)
yellowcanvas = Canvas(main, width=50, height=50, bg="black")
yellow = yellowcanvas.create_oval(1, 1, 50, 50, fill="yellow")
yellowcanvas.grid(row=1, column=0)
redcanvas = Canvas(main, width=50, height=50, bg="black")
red = redcanvas.create_oval(1, 1, 50, 50, fill="red")
redcanvas.grid(row=2, column=0) """


testbutton = Button(main, text="Testmodus", command= lambda: Ampel1.testmodus())
testbutton.grid(row=0, column=1)
debugbutton = Button(main, text="Schalten", command=lambda: Ampel1.schalten())
debugbutton.grid(row=0, column=2)

Ampel1 = Auto_Ampel()
Ampel1.initialize(0, 0)

Ampel2 = Auto_Ampel()
Ampel2.initialize(1, 0)



main.mainloop()