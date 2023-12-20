from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import Port




class Main_Controler:
  initiated = False
  ev3 = None
  xAchse = None
  yAchse = None
  zAchse = None

  pen_down = False
  
  x_cord = 0
  y_cord = 0

  def __init__(self, xAchse = Motor(Port.C), yAchse = Motor(Port.B), zAchse = Motor(Port.A)) -> None:
    global initiated
    Main_Controler.initiated = True 
    self.ev3 = EV3Brick()

    self.xAchse = xAchse
    self.yAchse = yAchse
    self.zAchse = zAchse
 

  def to(self, x, y):
    new_x = x + self.x_cord
    new_y = y + self.y_cord

  def move_diagonal():
    pass
  def point():
    pass 
  def line():
    pass 

  
