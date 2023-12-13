#!/usr/bin/env pybricks-micropython
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
import threading

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#360 = 45,24
# 360 / 45.24=7.95756

# 7.95756*50=397.878
# ein mm = 8 

# Create your objects here.
ev3 = EV3Brick()
# y_achse = Motor(Port.A)
# z_achse = Motor(Port.B)
# x_achse = Motor(Port.C)
# y_achse.run_target(500, 1000)
# time.sleep(0.5)
# test_motor.run_target(500, 10)
# y_achse.reset_angle()
# test_motor.run_target(

# def up():
#   z_achse.run_target(500, 0)
# def donw():
#   z_achse.run_target(500, 180)

#aufgabe1(ev3)

def einziehen(ev3):
    yAchse = Motor(Port.A)
    zAchse = Motor(Port.B)
    xAchse = Motor(Port.C)

    sensorColor = ColorSensor(Port.S1)
    sensorTouch = TouchSensor(Port.S2)

    xAchse.run(250)
    while not sensorTouch.pressed():
        pass
    xAchse.hold()

    yAchse.run(-250)
    while sensorColor.reflection() < 50:
        pass
    yAchse.hold()

def schreiben(ev3,write:bool)->bool:
    zAchse = Motor(Port.B)
    zAchse.run_angle(250, 180)
    return not write

"""class myThread(threading.Thread):
    def __init__(self, achse, name):
        threading.Thread.__init__(self)
        self.achse = achse
        self.name = name

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire(blocking = False)
        self.achse.run_time(-200,3000)
        threadLock.release()
        print("Exiting: " + self.name + "\n")


threadLock = threading.Lock()


print("hi")
ev3 = EV3Brick()
write = False

einziehen(ev3)
write = schreiben(ev3, write)

xAchse = Motor(Port.C)
yAchse = Motor(Port.A)

thread1 = myThread(yAchse, "Y Achse")
thread2 = myThread(xAchse, "X Achse")
thread1.start()
thread2.start()

print("Done main thread")

if write == True:
    write = schreiben(ev3, write)

yAchse.run_angle(250, 1000)"""

class myThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        print_time(self.name, 1,self.count)
        threadLock.release()
        print("Exiting: " + self.name + "\n")


def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print ("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1


threadLock = threading.Lock()

thread1 = myThread(1, "Thread 1", 5)
thread2 = myThread(2, "Thread 2", 5)


thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Done main thread")



    

