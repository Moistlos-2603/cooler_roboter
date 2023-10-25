def grad_y(mm):
    d = 43.2
    u = d * 3.1415926535
    v = 1/3

    grad = mm * 360 / v / u
    print(grad)

def grad_x(mm):
    u = 124
    v = 1/3

    grad = mm * 360 / v / u
    print(grad)

if __name__ == "__main__":
    grad_y(1)
    grad_x(1)
