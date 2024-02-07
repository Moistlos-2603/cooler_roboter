from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import Port
from pybricks.parameters import Direction
import _thread
import time
from module import muski
from berechnen import Reifen
import uasyncio as asyncio

class Main_Controler:
  initiated = False
  ev3 = None
  xAchse = None
  yAchse = None
  zAchse = None

  sensorColor = None
  sensorTouch = None

  xAchse_rechner = Reifen(1/3, umfang = 124)
  yAchse_rechner = Reifen(1/3, durchmesser = 43.2)

  
  x_cord = 0
  y_cord = 0

  
  def __init__(self, 
               xAchse = Motor(Port.C, positive_direction= Direction.CLOCKWISE), 
               yAchse = Motor(Port.B, positive_direction= Direction.COUNTERCLOCKWISE), 
               zAchse = Motor(Port.A), 
               sensorColor = ColorSensor(Port.S2),
               sensorTouch = TouchSensor(Port.S1)
              ) -> None:
    global initiated
    Main_Controler.initiated = True 
    self.ev3 = EV3Brick()

    self.xAchse = xAchse
    self.yAchse = yAchse
    self.zAchse = zAchse
    self.x_thread_finished = False
    self.y_thread_finished = False
    self.sensorColor = sensorColor
    self.sensorTouch = sensorTouch

  def thread_run_time(self, achse, name, speed, time_ms):
    print("Starting: " + name + "  speed: "+ str(speed)+ "  time" +str(time_ms)+"\n")
    # print(achse + "\n")
    achse.run_time(int(speed), int(time_ms))
    print("Exiting: " + name + "\n")
    if name == "X Achse":
      self.x_thread_finished = True
    else:
      self.y_thread_finished = True

  def thread_muski(self, ev3):
    muski.alle_meine_entchen(ev3)

  def start_musik(self):
    _thread.start_new_thread(self.thread_muski, (self.ev3))

  def to_alt(self, x, y, max_speed=100) -> None:
    delt_x = x - self.x_cord
    delt_y = y - self.y_cord
    self.x_cord = x
    self.y_cord = y

    if delt_x == 0 and delt_y == 0:
      return None

    if abs(delt_x) > abs(delt_y):
      x_speed = -max_speed
      y_speed = -((max_speed/self.xAchse_rechner.mm_to_grad(delt_x)) * self.yAchse_rechner.mm_to_grad(delt_y))
      run_time = abs((self.xAchse_rechner.mm_to_grad(delt_x)/max_speed) * 1000)

      _thread.start_new_thread(self.Thread_run_time, (self.xAchse, "Y Achse", x_speed, run_time))
      _thread.start_new_thread(self.Thread_run_time, (self.yAchse, "X Achse", y_speed, run_time))
      

    elif abs(delt_x) == abs(delt_y) :
      _thread.start_new_thread(self.Thread_run_time, (self.xAchse, "Y Achse", x_speed, run_time))
      _thread.start_new_thread(self.Thread_run_time, (self.yAchse, "X Achse", y_speed, run_time))
    else:
      x_speed = -((max_speed/self.yAchse_rechner.mm_to_grad(delt_y)) * self.xAchse_rechner.mm_to_grad(delt_x))
      y_speed = -max_speed
      run_time = abs((self.xAchse_rechner.mm_to_grad(delt_y)/max_speed) * 1000)

      _thread.start_new_thread(self.Thread_run_time, (self.xAchse, "Y Achse", x_speed, run_time))
      _thread.start_new_thread(self.Thread_run_time, (self.yAchse, "X Achse", y_speed, run_time))
      
  def to(self, x, y, max_speed= 50) -> None:
    delt_x_grad = self.xAchse_rechner.mm_to_grad(x - self.x_cord)
    delt_y_grad = self.yAchse_rechner.mm_to_grad(y - self.y_cord)
    self.x_cord = x
    self.y_cord = y

    

    if delt_x_grad == 0 and delt_y_grad == 0:
      return None
    
    elif delt_x_grad == 0:
      y_speed = max_speed if delt_y_grad > 0 else -max_speed
      run_time = abs((delt_y_grad/max_speed) * 1000)
      _thread.start_new_thread(self.thread_run_time, (self.yAchse, "Y Achse", y_speed, run_time))
      while not self.y_thread_finished:
        pass
      self.y_thread_finished = False

    elif delt_y_grad == 0:
      x_speed = max_speed if delt_x_grad > 0 else -max_speed
      run_time = abs((delt_x_grad/max_speed) * 1000)
      _thread.start_new_thread(self.thread_run_time, (self.xAchse, "X Achse", x_speed, run_time))
      while not self.x_thread_finished:
        pass
      self.x_thread_finished = False

    else:
      run_time= 0
      x_speed = 0
      y_speed = 0
      if abs(delt_x_grad) > abs(delt_y_grad):
        x_speed = max_speed if delt_x_grad > 0 else -max_speed
        y_speed = (max_speed/abs(delt_x_grad)) * delt_y_grad
        run_time = abs((delt_x_grad/max_speed) * 1000)
      else:
        x_speed = (max_speed/abs(delt_y_grad)) * delt_x_grad
        y_speed = max_speed if delt_y_grad > 0 else -max_speed
        run_time = abs((delt_y_grad/max_speed) * 1000)
        
      _thread.start_new_thread(self.thread_run_time, (self.yAchse, "Y Achse", y_speed, run_time))
      _thread.start_new_thread(self.thread_run_time, (self.xAchse, "X Achse", x_speed, run_time))
      while (not self.x_thread_finished) or (not self.y_thread_finished):
        pass
      self.x_thread_finished = False
      self.y_thread_finished = False
      
      

  def point(self, x, y):
    self.to(x,y)
    time.sleep(5)
    self.pen_up_or_down()
    self.pen_up_or_down()

  def pen_up_or_down(self):
    print("pen up or donw")
    self.zAchse.run_angle(100, 180)
    time.sleep(0.5)

  def line(self, x1, y1, x2, y2):
    self.to(x1,y1)
    self.pen_up_or_down()
    self.to(x2, y2)
    self.pen_up_or_down()

  def einziehen(self):
    self.yAchse.run(250)
    while self.sensorColor.reflection() < 50:
        pass
    self.yAchse.hold()

  def zero(self):
    # sorgt dafür das wir genau wissen wo die X Achse ist
    self.xAchse.run(250)
    while not self.sensorTouch.pressed():
        pass
    self.xAchse.hold()
    # Bringt X Achse an die start situation 
    self.run_x_grad(-1300)

    # sorgt dafür das wir genau wissen wo die Y Achse ist
    self.einziehen()
    self.yAchse.run(-250)
    while self.sensorColor.reflection() > 50:
      pass
    self.yAchse.hold()
    # Bringt Y Achse an die start situation 
    self.run_y_grad(-200)

  def run_x_grad(self, grad):
    self.xAchse.run_angle(500,grad)
    time.sleep(0.5)

  def run_y_grad(self, grad):
    self.yAchse.run_angle(500,grad)
    time.sleep(0.5)

  def run_z_grad(self, grad):
    self.zAchse.run_angle(100,grad)
    time.sleep(0.5)
