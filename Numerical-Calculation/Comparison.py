import numpy as np
import matplotlib.pyplot as plt
from lib.Model import *
plt.rcParams.update({
    "font.family": "Times New Roman",
    "font.size": 13,
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{amsfonts}",
    "lines.linewidth": 1
})

t = np.arange(0,10,0.01)
(k1, k2, k3) = (1.0, 20.0, 100.0)
(m1, m2) = (1.0, 1.0)
(x1_i,x2_i) = (-2,1)

# numerical solution
(x1,x2,v1,v2) = Numerical_Model(t, k=(k1, k2, k3),m=(m1, m2),x1_i=x1_i,x2_i=x2_i,v1_i=0,v2_i=0)
(X1,X2,V1,V2) = Analytical_Model(t, k=(k1, k2, k3),m=(m1, m2),x1_i=x1_i,x2_i=x2_i,v1_i=0,v2_i=0)

# --- plot -----------------------------------------------------------------------------
fig = plt.figure(figsize=(12,8),dpi=100)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
marker1 = '-'
marker2 = ':'
zorder1 = 1
zorder2 = 2
linewidth1 = 1
linewidth2 = 1.5
ax1.plot(t,x1,marker1   ,color='red',  label='numerical solution of $x_1$',  linewidth=linewidth1,zorder=zorder1)
ax1.plot(t,X1,marker2 ,color='black', label='eigenmode expansion of $x_2$', linewidth=linewidth2,zorder=zorder2)

ax2.plot(t,x2,marker1   ,color='blue',  label='numerical solution of $x_2$',  linewidth=linewidth1,zorder=zorder1)
ax2.plot(t,x2,marker2 ,color='black', label='eigenmode expansion of $x_2$', linewidth=linewidth2,zorder=zorder2)

[[[ax1,ax2][i].set_xlabel("$t$"),[ax1,ax2][i].set_ylabel(f"$x_{i+1}$")] for i in [0,1]]
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
fig.tight_layout()
plt.show()