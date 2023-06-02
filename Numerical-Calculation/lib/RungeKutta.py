import numpy as np

def RK1(f,y_0,x,h):
    y = np.zeros([len(x),len(y_0)])
    y[0] = y_0
    for i in range(0,len(x)-1):
        y[i+1] = y[i] + h * f(x[i],y[i])
    return y

def RK2(f,y_0,x,h):
    b1, b2 = 1/2, 1/2
    c1, c2 = 0, 1
    a21 = 1
    y = np.zeros([len(x),len(y_0)])
    y[0] = y_0
    for i in range(0,len(x)-1):
        f1 = f(x[i] + c1*h, y[i])
        f2 = f(x[i] + c2*h, y[i] + h*a21*f1)
        y[i+1] = y[i] + h * (b1*f1 + b2*f2)
    return y

def RK3(f,y_0,x,h):
    b1, b2, b3 = 1/6, 2/3, 1/6
    c1, c2, c3 = 0, 1/2, 1
    a21 = 1/2
    a31, a32 = -1, 2
    y = np.zeros([len(x),len(y_0)])
    y[0] = y_0
    for i in range(0,len(x)-1):
        f1 = f(x[i] + c1*h, y[i])
        f2 = f(x[i] + c2*h, y[i] + h*a21*f1)
        f3 = f(x[i] + c3*h, y[i] + h*a31*f1 + h*a32*f2)
        y[i+1] = y[i] + h * (b1*f1 + b2*f2 + b3*f3)
    return y

def RK4(f,y_0,x,h):
    b1, b2, b3, b4 = 1/6, 1/3, 1/3, 1/6
    c1, c2, c3, c4 = 0, 1/2, 1/2, 1
    a21           = 1/2
    a31, a32      = 0, 1/2
    a41, a42, a43 = 0, 0, 1
    y = np.zeros([len(x),len(y_0)])
    y[0] = y_0
    for i in range(0,len(x)-1):
        f1 = f(x[i] + c1*h, y[i])
        f2 = f(x[i] + c2*h, y[i] + h*a21*f1)
        f3 = f(x[i] + c3*h, y[i] + h*a31*f1 + h*a32*f2)
        f4 = f(x[i] + c4*h, y[i] + h*a41*f1 + h*a42*f2 + h*a43*f3)
        y[i+1] = y[i] + h * (b1*f1 + b2*f2 + b3*f3 + b4*f4)
    return y

def RK5(f,y_0,x,h):
    b1 ,b2 ,b3 ,b4, b5  = 1/6, 0, 0, 2/3, 1/6
    c1, c2, c3, c4, c5  = 0, 1/3, 1/3, 1/2, 1
    a21                 = 1/3  
    a31, a32            = 1/6,  1/6
    a41, a42, a43       = 1/8,  0,   3/8
    a51, a52, a53, a54  = 1/2,  0,   -3/2, 2
    y = np.zeros([len(x),len(y_0)])
    y[0] = y_0
    for i in range(0,len(x)-1):
        f1 = f(x[i] + c1*h, y[i])
        f2 = f(x[i] + c2*h, y[i] + h*a21*f1)
        f3 = f(x[i] + c3*h, y[i] + h*a31*f1 + h*a32*f2)
        f4 = f(x[i] + c4*h, y[i] + h*a41*f1 + h*a42*f2 + h*a43*f3)
        f5 = f(x[i] + c5*h, y[i] + h*a51*f1 + h*a52*f2 + h*a53*f3 + h*a54*f4)
        y[i+1] = y[i] + h * (b1*f1 + b2*f2 + b3*f3 + b4*f4 + b5*f5)
    return y

def RKF45(f, y_0, x, h):
    c = [0, 1/4, 3/8, 12/13, 1, 1/2]
    a = [
        [0],
        [1/4, 0],
        [3/32, 9/32, 0],
        [1932/2197, -7200/2197, 7296/2197, 0],
        [439/216, -8, 3680/513, -845/4104, 0],
        [-8/27, 2, -3544/2565, 1859/4104, -11/40]
    ]
    b_rk4 = [25/216, 0, 1408/2565, 2197/4104, -1/5, 0]
    b_rk5 = [16/135, 0, 6656/12825, 28561/56430, -9/50, 2/55]

    y = np.zeros([len(x), len(y_0)])
    y[0] = y_0
    for i in range(0, len(x) - 1):
        k = np.zeros([6, len(y_0)])
        for j in range(6):
            f_sum = np.zeros(len(y_0))
            for l in range(j):
                f_sum += a[j][l] * k[l]
            k[j] = f(x[i] + c[j] * h, y[i] + h * f_sum)

        y_rk4 = y[i] + h * np.dot(b_rk4, k)
        y_rk5 = y[i] + h * np.dot(b_rk5, k)
        error = np.abs(y_rk5 - y_rk4)
        tolerance = 1e-12 + np.maximum(np.abs(y_rk5), np.abs(y_rk4)) * 1e-8
        delta = np.maximum(error / tolerance, 1e-10)
        h_next = h / delta**0.2

        if np.all(delta <= 1):
            y[i + 1] = y_rk5
            h = h_next
        else:
            h = h_next

    return y

