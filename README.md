# Coupled Oscillators
This Repository is for my final project in **Experiments on Fundamental Physics(II)** course at Chung Cheng University. The objective is to use [Arduino](https://www.arduino.cc/) to create an instrument for a general physics experiment. Specifically, I aim to analyze the oscillatory behavior of two objects, $m_1$ and $m_2$, under three different springs with spring constant $k_1$, $k_2$ and $k_3$ using a laser rangefinder and an ultrasonic rangefinder (as shown in the diagram).

<p align="center">
<img width="500px" src="./Theoretical-Calculation/System-Figure/figure.svg" alt="">
</p>

## Theoretical Calculations
[📄 Research Paper](./Theoretical-Calculation/Coupled-Oscillators.pdf)

In the theoretical calculations section (`./Theoretical-Calculation/`), I have constructed the Lagrangian of the system and used the [Euler-Lagrange equations](https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation) to derive the equations of motion for the objects

$$
\begin{equation}
\begin{pmatrix} 
\ddot{x}_1\\ 
\ddot{x}_2
\end{pmatrix}=
\begin{pmatrix}
\displaystyle - \frac{k_1+k_2}{m_1}	&\displaystyle  \frac{k_2}{m_1}\\ 
\displaystyle  \frac{k_2}{m_2} &\displaystyle -\frac{k_2+k_3}{m_2}
\end{pmatrix} 
\begin{pmatrix}
x_1\\ 
x_2
\end{pmatrix}.
\end{equation}
$$

Finally, I have employed linear expansion for Eigenmodes

$$
\psi(t) = \sum_{i=1}^{2}C_ie^{i\omega_it}\mu_{i}
$$

to compute the results and compared them with the numerical calculations.


## Numerical Calculations
For the numerical calculations (`./Numerical-Calculation/`), I have utilized Python as the programming language for computations and plotting. [Jupyter Notebook](https://jupyter.org/) has been employed as the execution environment for running the Python code.

