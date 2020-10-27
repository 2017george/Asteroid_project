from tkinter import *
from ship import *
from beam import *
from health import *

class Game():
    def __init__(self, canvas, root, background_list):
        self.canvas = canvas
        self.root = root
        self.background_list =background_list

        #binds for key presses
        root.bind('<KeyPress>',  self.onkeypress)
        root.bind('<Button-1>', self.onmouse)

        #create a call to run the other classes
        self.asteroidship = ship(0, self.canvas.winfo_reqheight()//2, self.canvas)
        self.health = health(self.canvas)
        #create vars that will be used in this class
        self.beam_num = 5
        self.beam_avalible = []

        #run setup functions
        self.__beams()
    def __beams(self):
        for i in range(self.beam_num):
            self.beam_avalible.append(Beam(self.canvas))
    def onkeypress(self, event):
        pos = self.asteroidship.getLocation()
        if event.char == "w":
            if not pos[2] <= 70:
                self.asteroidship.move(y=-20)
            else:
                pass
        elif event.char == "a":
            if not pos[0] <= 0:
                self.asteroidship.move(x=-20)
            else:
                pass
        elif event.char == "s":
            if not pos[3]+20 >= self.canvas.winfo_reqheight():
                self.asteroidship.move(y=20)
            else:
                pass
        elif event.char == "d":
            if not pos[1]+5 >= self.canvas.winfo_reqwidth():
                self.asteroidship.move(x=20)
            else:
                pass
    def onmouse(self, event):
        print("casualty")
        self.beam_num -= 1
        self.beam_avalible[self.beam_num].shoot(self.asteroidship.getX(), self.asteroidship.getY())
        if self.beam_num == -1:
            self.beam_num = 4
            print (self.beam_avalible)
        #Shoot the bullet :D
    def checkCollision(self, event):
        pass


    def exit_program(self):
        quit()
