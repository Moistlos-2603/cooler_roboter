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

aufgabe1(ev3)
  


