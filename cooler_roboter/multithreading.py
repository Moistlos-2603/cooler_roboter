import threading
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

from module.muski import alle_meine_entchen
from module.aufgaben import aufgabe1
from berechnen import *
from main import *


class myThread(threading.Thread):
    def __init__(self, achse, name):
        threading.Thread.__init__(self)
        self.achse = achse
        self.name = name

    def run(self):
        print("Starting: " + self.name + "\n")
        self.achse.run_time(-200,3000)

        print("Exiting: " + self.name + "\n")

def zeug():

    print("hi")
    ev3 = EV3Brick()

    write = True

    write = schreiben(ev3, write)

    einziehen(ev3)

    write = schreiben(ev3, write)

    xAchse = Motor(Port.C)
    yAchse = Motor(Port.A)

    thread1 = myThread(yAchse, "Y Achse")
    thread2 = myThread(xAchse, "X Achse")


    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Done main thread")

    if write == True:
        write = schreiben(ev3, write)

    yAchse.run_angle(250, 1000)