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
from buildhat import *

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
    print(sensorColor.reflection())

def schreiben(ev3,write:bool)->bool:
    zAchse = Motor(Port.B)
    zAchse.run_angle(250, 180)
    return not write

schreiben(ev3,True)


einziehen(ev3)
write = False

write = schreiben(ev3, write)


xAchse = Motor(Port.C)
yAchse = Motor(Port.A)

pair = MotorPair(yAchse, xAchse)

pair.set_default_speed(500)
pair.run_for_degrees(720)

"""
X = Reifen(1/3, umfang = 124)
Y = Reifen(1/3, durchmesser = 43.2)

write = schreiben(ev3, write)

distanzX = X.grad(-20)
distanzY = Y.grad(-20)

xAchse.run_angle(250, distanzX)
yAchse.run_angle(250, distanzY)
"""

#yAchse.run_time(-200, 3000, wait=False)
#xAchse.run_time(-200,3000)


if write == True:
    write = schreiben(ev3, write)

time.sleep(2)

yAchse.run_angle(250, 1000)


    

