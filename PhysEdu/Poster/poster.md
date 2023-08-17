
# Parameter Estimation of Coupled Oscillation System through Markov Chain Monte Carlo Method

- **Authors:** Chang-Mao Yang, Pi-Hui Tuan
- **Affiliation:** National Chung Cheng University, Department of Physics
- **Contact:** 409220055@alum.ccu.edu.tw

## Introduction:

Parameter estimation is crucial in scientific research, especially in data analysis and modeling. Traditional optimization techniques, such as the least square method, often face challenges with increasing parameter dimensionality. The Markov Chain Monte Carlo (MCMC) method, particularly its Metropolis-Hastings variant, emerges as a powerful alternative, with applications in areas like gravitational wave data analysis.

In this context, coupled oscillators, which offer insights into phenomena like lattice vibrations, become an interesting subject of study. We constructed an experimental system of oscillators connected through springs with unknown constants. Using the MCMC method, we aimed to estimate these unknown spring constants. Our results indicate that MCMC not only enhances computational efficiency but also provides more accurate parameter estimations compared to traditional methods.

## Experimental Equipment:

Our experimental setup, depicted in a provided figure, consists of a standard pulley track and two frictionless carts. These carts are interconnected using three homemade springs crafted from white iron wire, forming a coupled oscillator system. To capture the oscillators' motion, we employed two ultrasonic distance sensors, housed in 3D-printed frames and connected to an Arduino circuit board. Furthermore, we developed a customized webpage hosted on GitHub for real-time visualization of the displacement data recorded by these sensors. This setup enabled us to measure and document the dynamics of the coupled oscillators effectively.

## Analytical Model:

Our experimental equipment can be interpreted as shown in FIG. ().

The system's Lagrangian is represented by 
$$
\mathcal{L} = \frac{1}{2}\sum_{i=1}^{2}m_i \frac{d^2x_i}{dt^2}
		-\frac{k_1x_1^2+k_2\left(x_1-x_2\right)^2+k_3x_2^2}{2},
$$
where $m_i$ is the mass of $i^{\rm th}$ oscillator and $\left(k_1,k_2,k_3\right)$ are the spring constants. Using Euler-Lagrange equation, we obtain a set of the second-order differential equations
$$
\frac{d^2}{dt^2}\begin{pmatrix}x_1\\ x_2\end{pmatrix} =
\begin{pmatrix}
\displaystyle - \frac{k_1+k_2}{m_1}	&\displaystyle  \frac{k_2}{m_1}\\[2ex]
\displaystyle  \frac{k_2}{m_2} 		&\displaystyle  -\frac{k_2+k_3}{m_2}
\end{pmatrix}
\begin{pmatrix}x_1\\ x_2\end{pmatrix}.
$$
After some algebra, the general expressions for the time-dependent displacement $x_1\left(t\right)$ and $x_2\left(t\right)$ can be exactly solved.

---

## Desired Distribution:

Given the system parameters and initial conditions, the displacements $x_1(t)$ and $x_2(t)$ of the coupled oscillators can be determined. After measuring the masses and initial positions of the oscillators, the real-time data can be used to estimate the unknown spring constants $k_1$, $k_2$ and $k_3$. The fitting error is defined as:
$$
\mathrm{err}(k_1,k_2,k_3) = \sum_{i=1}^{2}\sum_{j=0}^{N-1}\frac{(x_i(t_j) - x_{i,j})^2}{N},
$$
where $N$ is the total time steps. The desired distribution for optimization is:
$$
p(k_1,k_2,k_3) = \exp(-\text{err}(k_1,k_2,k_3)),
$$
Optimized values for $(k_1)$, $k_2$, and $k_3$ correspond to the distribution's maximum. To enhance optimization accuracy, we applied a Gamma correction to improve the distribution's contrast.

## MCMC Method and Results:

Using the defined distribution function $P$, we applied the Metropolis-Hastings algorithm within the MCMC method to explore the parameter space of $\left(k_1,k_2,k_3\right)$. After sampling $100,000$ combinations, we obtained a simulated posterior distribution, as shown in FIG. (\ref{fig:MCMC_corner}). The distributions for the spring constants $k_1$, $k_2$, and $k_3$ resemble normal distributions, ensuring accurate estimations. 

![](paper/image/MCMC_corner.pdf)

The comparison between experimental measurements and numerical calculations based on MCMC-estimated parameters is presented in FIG. (\ref{fig:position_compare}), highlighting the method's effectiveness.

![](paper/image/position_compare.pdf)



## Conclusion:
We applied the MCMC method, particularly the Metropolis-Hastings algorithm, to the coupled oscillators system. Through this method, we explored the parameter space of the spring constants $k_1$, $k_2$, and $k_3$, achieving a posterior distribution resembling a normal distribution.

Despite some experimental discrepancies, the MCMC results aligned well with the experimental data. Our findings highlight the MCMC method's superiority over traditional techniques in parameter estimation for complex systems.

Future endeavors will aim to refine the experimental process and delve deeper into the system's dynamics by considering springs with varied elastic constants. This will further our understanding of coupled oscillators and pave the way for enhanced models and analytical methods.

---

## Footer:

- **References:** List the most crucial references, using QR codes for direct access.
- **Contact Information:** Provide a QR code linking to the full paper or more detailed information.
