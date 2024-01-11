import math
from main_controler import Main_Controler
import random 

class Chaosgame():
  def __init__(self, ) -> None:
    pass
  
  def first_point(self):
    pass

  def game(self):
    pass

  def new_pos(self):
    pass

  def check_if_inside(self):
    pass

  def area(self):
    pass
  
 


class Chaosgame_Dreieck(Chaosgame):
  controler = None
  init_punkt1 = (0,0)
  init_punkt2 = (0,0)
  init_punkt3 = (0,0)

  point = (None, None)
  
  def __init__(self, 
               init_punkte = ((250, 50), (150, 200), (350, 200))
               
               ) -> None:
    self.controler = Main_Controler()
    self.init_punkt1 = init_punkte[0]
    self.init_punkt2 = init_punkte[1] 
    self.init_punkt3 = init_punkte[2]

    print("1")
    self.controler.point(*self.init_punkt1)
    print("2")
    self.controler.point(*self.init_punkt2)
    print("3")
    self.controler.point(*self.init_punkt3)

    self.controler.einziehen()
    self.controler.zero()


    self.first_point()

  def first_point(self):
    not_inside = True
    while not_inside:
      a = int(self.init_punkt2[0])
      b = int(self.init_punkt3[0])
      c = int(self.init_punkt2[1])
      d = int(self.init_punkt1[1])
      print(str(a) + ", " +str(b)+ ", " +str(c)+ ", " +str(d))
      first_point = (random.randint(a,b), 
                     random.randint(c,d))
      if self.check_if_inside(first_point):
        not_inside = False
        self.controler.point(*first_point)
        point = first_point

  def game(self, iterations = 1000):
    eckpunkte = {0 : self.init_punkt1, 1:self.init_punkt2, 2:self.init_punkt3}
    for i in range(iterations):
      print(i)
      point_id = random.randint(0, 2)
      self.point = self.new_pos(self.point, eckpunkte[point_id])
      self.controler.point(self.point)

  def new_pos(self, point0:(int, int), point1:(int, int)):
    return (
      # X
      int(abs( (point0[0] - point1[0]) /2  + point1[0])) ,
      # Y
      int(abs( (point0[1] - point1[1]) /2  + point1[1]))
      )


  
  def check_if_inside(self, point):
    point0 = self.init_punkt1
    point1 = self.init_punkt2
    point2 = self.init_punkt3

    # ABC
    A = self.area(point0, point1, point2)
    # PBC
    A1 = self.area(point, point1, point2)
    # PAC
    A2 = self.area(point0, point, point2)
    # PAB
    A3 = self.area(point0, point1, point)
    if(A == (A1 + A2 + A3)):
      return True
    else:
      return False
  
  def area(self, point0:(int, int), point1:(int, int), point2:(int, int)):
    x0 = point0[0]
    y0 = point0[1]
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    
    return abs((x0*(y1-y2)+x1*(y2-y0)+x2*(y0-y1))/2)