def grad_y(mm:int)->int:
    durchmesser = 43.2
    umfang = durchmesser * 3.1415926535
    verhältnis = 1/3

    grad = mm * 360 / verhältnis / umfang
    print(grad)
    return grad

def grad_x(mm:int)->int:
    umfang = 124
    verhältnis = 1/3

    grad = mm * 360 / verhältnis / umfang
    print(grad)
    return grad

if __name__ == "__main__":
    grad_y(1)
    grad_x(1)
