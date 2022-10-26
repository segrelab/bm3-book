# Numerical Solution

## Example
Suppose a company manufactures different electronic components for computers. Component A requires 2
hours of fabrication and 1 hour of assembly; component B requires 3 hours of fabrication and 1 hour of assembly,
and component C requires 2 hours of fabrication and 2 hours of assembly. The company has up to 1,000 labor
hours for fabrication and 800 labor-hours of assembly time each week. If the profit on each component A, B, and
C is \$7, \$8, \$10 respectively, how many of each should be produced to maximize profit?

### 1. Collect information
Rewrite the information in the problem in the general form of an optimization problem as follows:

minimize (or maximize) $f(x)$

subject to

$h(x) = 0$

$g(x) \leq 0$

$x \in S$

```{admonition} Click to show the solution
:class: tip, dropdown
maximize $7x_1 + 8x_2 + 10x_3$

subject to

$x_1, x_2, x_3 \geq 0$

$2x_1 + 3x_2 + 2x_3 \leq 1,000$

$1x_1 + 1x_2 + 2x_3 \leq 800$

where $x_1$ is the number of components of type A

where $x_2$ is the number of components of type B

where $x_3$ is the number of components of type C
```

### 2. Rearrange equations to introduce positive slack variables

Get all variables of the objective function on one side of the equation.
```{admonition} Click to show the solution
:class: tip, dropdown
$p = 7x_1 + 8x_2 + 10x_3$

$-7x_1 + -8x_2 + -10x_3 + p = 0$
```

Add a positive slack variable to the fabrication time constraint.
```{admonition} Click to show the solution
:class: tip, dropdown
$2x_1 + 3x_2 + 2x_3 \leq 1,000$

$2x_1 + 3x_2 + 2x_3 + s_1 = 1,000$
```

Add a positive slack variable to the assembly time constraint.
```{admonition} Click to show the solution
:class: tip, dropdown
$1x_1 + 1x_2 + 2x_3 \leq 800$

$1x_1 + 1x_2 + 2x_3 + s_2 = 800$
```
### 3. Set-up the simplex tableau

\begin{bmatrix}1 & x_{1}\\
1 & x_{2}\\
1 & x_{3}
\end{bmatrix}$$
