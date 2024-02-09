from PIL import Image, ImageDraw
import random 
import math

def setup(brightness=255):
  img = Image.new('RGB', (500, 300), (brightness, brightness, brightness))
  return ImageDraw.Draw(img), img

def area_triengel(point0, point1, point2):
  x0 = point0[0]
  y0 = point0[1]
  x1 = point1[0]
  y1 = point1[1]
  x2 = point2[0]
  y2 = point2[1]
  # return (x0*(y1-y2)+x1*(y2-y0)+x2*(y0-y1))/2
  return abs((x0*(y1-y2)+x1*(y2-y0)+x2*(y0-y1))/2)
  
def check_if_in_triengel(point0:(int, int), point1:(int, int), point2:(int, int), point:(int, int)):
  # ABC
  A = area_triengel(point0, point1, point2)
  # PBC
  A1 = area_triengel(point, point1, point2)
  # PAC
  A2 = area_triengel(point0, point, point2)
  # PAB
  A3 = area_triengel(point0, point1, point)
  if(A == (A1 + A2 + A3)):
    return True
  else:
    return False

def distens(point0:(int, int), point1:(int, int)):
  return math.sqrt((point0[0]-point1[0])**2 + (point0[0]-point1[1])**2)

def new_pos(point0:(int, int), point1:(int, int)):
  return (
    # X
    int(abs( (point0[0] - point1[0]) /2  + point1[0])) ,
    # Y
    int(abs( (point0[1] - point1[1]) /2  + point1[1]))
    )



draw, img = setup()

# Init points
point0 = (250, 50)
point1 = (150, 200)
point2 = (350, 200)

draw.point(point0, fill=(255, 0, 0))
draw.point(point1, fill=(255, 0, 0))
draw.point(point2, fill=(255, 0, 0))


Point = (random.randint(150, 350), random.randint(50, 200))
if check_if_in_triengel(point0, point1, point2, Point):
  draw.point(Point, fill=(0, 0, 0))
else:
  Point = (250, 100)
  draw.point(Point, fill=(0, 0, 0))


for i in range(100000):


  point_id = random.randint(0, 2)
  eckpunkt =()
  if point_id == 0:eckpunkt = point0
  elif point_id == 1:eckpunkt = point1
  elif point_id == 2:eckpunkt = point2

  Point = new_pos(Point, eckpunkt)  
  print(Point)
  draw.point(Point, fill=(0, 0, 0))

  


  
img.show()