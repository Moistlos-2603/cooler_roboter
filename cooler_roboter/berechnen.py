import math;

#y: durchmesser = 43.2, verhältnis = 1/3
#x: umfang = 124, verhältnis = 1/3

class Reifen:
    def __init__(self, verhältnis:float, umfang=0.0, durchmesser=0.0):
        self.verhältnis = verhältnis
        if umfang == 0:
            self.umfang = durchmesser*math.pi
        else:
            self.umfang = umfang

    def mm_to_grad(self, mm:int)->int:
        return int(mm * 360 / self.verhältnis / self.umfang)


if __name__ == "__main__":
    xAchse = Reifen(1/3, umfang = 124)
    yAchse = Reifen(1/3, durchmesser = 43.2)

    