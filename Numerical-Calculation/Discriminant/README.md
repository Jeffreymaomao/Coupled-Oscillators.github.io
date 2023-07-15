# Discriminant for the eigenvalues
## Analytic form
The eigenvalues for the system are given by
$$
\lambda_1,\lambda_2 = \frac{\mathrm{tr}(\mathcal{F}) \pm \sqrt{\mathrm{tr}(\mathcal{F})^2-4\det({\mathcal{F}})}}{2},
$$
where
$$
\begin{aligned}
\mathrm{tr}(\mathcal{F}) &=-\frac{m_2k_1+\left(m_1+m_2\right)k_2+m_1k_3}{m_1m_2}
\\
\det(\mathcal{F}) &=\frac{k_1k_2+k_2k_3+k_3k_1}{m_1m_2}.
\end{aligned}
$$
## 1st Discriminant
Define 1st discriminant to be 
$$
\Delta_1 = \mathrm{tr}(\mathcal{F})^2-4\det({\mathcal{F}}),
$$
the equation $\Delta_1>0$ can be reduced to 
$$
\frac{\left(k_{1} m_{2} + k_{2} \left(m_{1} + m_{2}\right) + k_{3} m_{1}\right)^{2}}{4 m_{1} m_{2} \left(k_{1} k_{2} + k_{1} k_{3} + k_{2} k_{3}\right)} > 0
$$
or
$$
\frac{\displaystyle k_{1}^{2} m_{2}^{2} + k_{2}^{2} \left(m_{1} + m_{2}\right)^{2} + 2 k_{2} \left(k_{1} m_{2}^{2} + k_{3} m_{1}^{2}\right) + k_{3}^{2} m_{1}^{2}}{2 m_{1} m_{2} \left(k_{1} k_{2} + k_{1} k_{3} + k_{2} k_{3}\right)} > 0
$$

<div style="color:red;text-align:center;border:solid 1px red;padding:10px">

After a lot of testing, I think the value for this discriminant $\Delta_1$ satisfy

$$
\Delta_1 > 0,\quad \forall k_1,k_2,k_3,m_1,m_2 >0
$$

</div>
