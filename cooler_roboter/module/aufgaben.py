from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color


def aufgabe1(ev3):
  y_achse = Motor(Port.A)
  z_achse = Motor(Port.B)
  x_achse = Motor(Port.C)
  # z_achse.run_angle(300, 180)

  # x_achse.run_angle(100, rotation_angle=-400)
  # y_achse.run_angle(50, rotation_angle=-800)
  # y_achse.run_angle(50, rotation_angle=10)
  y_achse.run_angle(700, rotation_angle=1000)


  # z_achse.run_angle(300, 180)


def aufgabe2(ev3):
  y_achse = Motor(Port.A)
  z_achse = Motor(Port.B)
  x_achse = Motor(Port.C)



  y_achse.run_angle(500, rotation_angle=-400)
  x_achse.run_angle(500, rotation_angle=-100)