import numpy as np
import matplotlib.pyplot as plt
from numpy import pi,sqrt,exp,cos,sin,array
from numpy.linalg import inv
from lib.Model import *
plt.rcParams.update({
    "font.family": "Times New Roman",
    "font.size": 13,
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{amsfonts}",
    "lines.linewidth": 1
})

dt = 0.01
t_end=60
(k1, k2, k3) = (1.0, 1.0, 1.0)
(m1, m2) = (1.0, 1.0)
(x1_i,x2_i) = (1,1)

# numerical solution
(t, x1,x2,v1,v2) = Model(k=(k1, k2, k3),m=(m1, m2),dt=dt,t_end=t_end,x1_i=x1_i,x2_i=x2_i,v1_i=0,v2_i=0)
# Eigenmode expansion
trF  = -(m2*k1 + (m1+m2)*k2 + m1*k3)/(m1*m2)
detF =  (k1*k2 + k2*k3 + k3*k1)/(m1*m2)
(lda1,lda2) = ((trF +sqrt(trF*trF-4*detF))/2, (trF -sqrt(trF*trF-4*detF))/2)
(omega1,omega2) = (sqrt(-lda1),sqrt(-lda2)) 
(mu1,mu2) = (array([[m2*lda1+(k2+k3)], [k2]]),array([[m2*lda2+(k2+k3)], [k2]]))
M = np.hstack([mu1,mu2])
invM = inv(M)
C = invM@array([[x1_i],[x2_i]])
(C1,C2) = (C[0][0],C[1][0])
psi = C1*cos(omega1*t)*mu1 + C2*cos(omega2*t)*mu2
(psi1,psi2) = (psi[0],psi[1])

step1 = 30
# --- plot -----------------------------------------------------------------------------
fig = plt.figure(figsize=(8,4),dpi=100)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
marker1 = '-'
marker2 = '--'
zorder1 = 1
zorder2 = 2
linewidth1 = 1
linewidth2 = 1.5
ax1.plot(t,x1,marker1   ,color='r',  label='numerical solution of $x_1$',  linewidth=linewidth1,zorder=zorder1)
ax1.plot(t,psi1,marker2 ,color='black', label='eigenmode expansion of $x_2$', linewidth=linewidth2,zorder=zorder2)

ax2.plot(t,x2,marker1   ,color='b',  label='numerical solution of $x_2$',  linewidth=linewidth1,zorder=zorder1)
ax2.plot(t,psi2,marker2 ,color='black', label='eigenmode expansion of $x_2$', linewidth=linewidth2,zorder=zorder2)

[[[ax1,ax2][i].set_xlabel("$t$"),[ax1,ax2][i].set_ylabel(f"$x_{i+1}$")] for i in [0,1]]
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
fig.tight_layout()
plt.show()