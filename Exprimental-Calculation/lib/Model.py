from numpy import exp,sqrt,array,zeros,hstack,real,arange

def RK1(f,y_0,x,h):
    y = zeros([len(x),len(y_0)])
    y[0] = y_0
    for i in range(0,len(x)-1):
        y[i+1] = y[i] + h * f(x[i],y[i])
    return y

def RK2(f,y_0,x,h):
    b1, b2 = 1/2, 1/2
    c1, c2 = 0, 1
    a21 = 1
    y = zeros([len(x),len(y_0)])
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
    y = zeros([len(x),len(y_0)])
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
    y = zeros([len(x),len(y_0)])
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
    y = zeros([len(x),len(y_0)])
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
    b1,b2,b3,b4,b5    = 25/216, 0, 1408/2565, 2197/4104, -1/5
    B1,B2,B3,B4,B5,B6 = 16/135, 0, 6656/12825, 28561/56430, -9/50, 2/55
    c1,c2,c3,c4,c5,c6 = 0, 1/4, 3/8, 12/13, 1, 1/2
    a21                          = 1/4
    a31, a32                     = 3/32, 9/32
    a41, a42, a43                = 1932/2197, -7200/2197, 7296/2197 
    a51, a52, a53, a54           = 439/216, -8, 3680/513, -845/4104 
    a61, a62, a63, a64, a65      = -8/27, 2, -3544/2565, 1859/4104, -11/40
    y = zeros([len(x), len(y_0)])
    y[0] = y_0
    for i in range(0,len(x)-1):
        f1 = f(x[i] + c1*h, y[i])
        f2 = f(x[i] + c2*h, y[i] + h*a21*f1)
        f3 = f(x[i] + c3*h, y[i] + h*a31*f1 + h*a32*f2)
        f4 = f(x[i] + c4*h, y[i] + h*a41*f1 + h*a42*f2 + h*a43*f3)
        f5 = f(x[i] + c5*h, y[i] + h*a51*f1 + h*a52*f2 + h*a53*f3 + h*a54*f4)
        f6 = f(x[i] + c6*h, y[i] + h*a61*f1 + h*a62*f2 + h*a63*f3 + h*a64*f4)
        y4 = y[i] + h*(b1*f1 + b2*f2 + b3*f3 + b4*f4 + b5*f5)
        y5 = y[i] + h*(B1*f1 + B2*f2 + B3*f3 + B4*f4 + B5*f5+ B6*f6)
        y[i+1] = y5
    return y

def Model(k=(1.0, 1.0, 1.0), m=(1.0, 1.0), dt=0.01, t_end=50, x1_i=-1, x2_i=1, v1_i=0, v2_i=0):
    """
    Parameters
    ----------
        k     : (<k1>, <k2>, <k3>)
        m     : (<m1>, <m2>)
        dt    : <time step size>
        t_end : <end of time>
        x1_i  : <initial position of m1>
        x2_i  : <initial position of m2>
        v1_i  : <initial velocity of m1>
        v2_i  : <initial velocity of m2>
    Returns
    -------
        t     : <time array>
        x1    : <position of masses m1 array>
        x2    : <position of masses m2 array>
        v1    : <velocity of masses m1 array>
        v2    : <velocity of masses m2 array>
    """
    (k1, k2, k3) = k
    (m1, m2) = m

    def F(t,U):
        (x1_,x2_,v1_,v2_) = (U[0],U[1],U[2],U[3])
        a1_ = -(k1 * x1_ + k2 * (x1_ - x2_))/m1
        a2_ = -(k3 * x2_ + k2 * (x2_ - x1_))/m2
        return array([v1_,v2_,a1_,a2_])
    
    t = arange(0,t_end,dt)
    U0 = array([x1_i,x2_i,v1_i,v2_i,]).T 
    U = RKF45(F, U0, t, dt)
    return (t, U[:,0],U[:,1],U[:,2],U[:,3]) # (t, x1, x2, v1, v2)

def Numerical_Model(t, k=(1.0, 1.0, 1.0), m=(1.0, 1.0), x1_i=-1, x2_i=1, v1_i=0, v2_i=0):
    """
    Parameters
    ----------
        t     : <time series>
        k     : (<k1>, <k2>, <k3>)
        m     : (<m1>, <m2>)
        dt    : <time step size>
        t_end : <end of time>
        x1_i  : <initial position of m1>
        x2_i  : <initial position of m2>
        v1_i  : <initial velocity of m1>
        v2_i  : <initial velocity of m2>
    Returns
    -------
        x1    : <position of masses m1 array>
        x2    : <position of masses m2 array>
        v1    : <velocity of masses m1 array>
        v2    : <velocity of masses m2 array>
    """
    dt = t[1] - t[0]
    (k1, k2, k3) = k
    (m1, m2) = m

    def F(t,U):
        (x1_,x2_,v1_,v2_) = (U[0],U[1],U[2],U[3])
        a1_ = -(k1 * x1_ + k2 * (x1_ - x2_))/m1
        a2_ = -(k3 * x2_ + k2 * (x2_ - x1_))/m2
        return array([v1_,v2_,a1_,a2_])
    U0 = array([x1_i,x2_i,v1_i,v2_i,]).T 
    U = RKF45(F, U0, t, dt)
    return U[:,0],U[:,1],U[:,2],U[:,3] # (x1, x2, v1, v2)

def Analytical_Model(t, k=(1.0, 1.0, 1.0), m=(1.0, 1.0), x1_i=-1, x2_i=1, v1_i=0, v2_i=0):
    """
    Parameters
    ----------
        t     : <time series>
        k     : (<k1>, <k2>, <k3>)
        m     : (<m1>, <m2>)
        x1_i  : <initial position of m1>
        x2_i  : <initial position of m2>
        v1_i  : <initial velocity of m1>
        v2_i  : <initial velocity of m2>
    Returns
    -------
        x1    : <position of masses m1 array>
        x2    : <position of masses m2 array>
        v1    : <velocity of masses m1 array>
        v2    : <velocity of masses m2 array>
    """
    (k1, k2, k3) = k
    (m1, m2) = m
    trF  = -(m2*k1+(m1+m2)*k2+m1*k3)/(m1*m2) # Trace of matrix F
    detF =  (k1*k2+k2*k3+k3*k1)/(m1*m2)      # Determinant of matrix F
    lda1 = (trF + sqrt(trF*trF - 4*detF))/2  # 1st Eigenvalue of matrix F
    lda2 = (trF - sqrt(trF*trF - 4*detF))/2  # 2nd Eigenvalue of matrix F

    omega1 = sqrt(lda1+0j) # 1st Eigenfrequency
    omega2 = sqrt(lda2+0j) # 2nd Eigenfrequency
    invOmega = array([[1.0/omega1,0.0], [0.0,1.0/omega2]]) # inverse of matrix diag([omega1, omega2])

    mu1 = array([[m2*lda1+(k2+k3)], [k2]]) # 1st Eigenvector of matrix F
    mu2 = array([[m2*lda2+(k2+k3)], [k2]]) # 2nd Eigenvector of matrix F
    
    detMu = k2*m2*(lda1-lda2)  # Determinant of matrix hstack([mu1, mu2])
    invMu = array([[k2,-m2*lda2-(k2+k3)],[-k2,m2*lda1+(k2+k3)]])/detMu # inverse of matrix hstack([mu1, mu2])

    xi0 = array([[x1_i], [x2_i]]) # initial condition for position
    vi0 = array([[v1_i], [v2_i]]) # initial condition for velocity

    C = hstack([invMu@xi0, invOmega@invMu@vi0]) @ array([[0.5,0.5],[0.5,-0.5]]) # Coefficient matrix

    (A1,B1,A2,B2) = (C[0,0],C[0,1],C[1,0],C[1,1])

    x = (A1*exp(omega1*t)+B1*exp(-omega1*t))*mu1 + (A2*exp(omega2*t)+B2*exp(-omega2*t))*mu2
    v = (A1*omega1*exp(omega1*t)-B1*omega1*exp(-omega1*t))*mu1 + (A2*omega2*exp(omega2*t)-B2*omega2*exp(-omega2*t))*mu2
    return real(x[0]), real(x[1]), real(v[0]), real(v[1])