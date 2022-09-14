# Fundamentals

This section will review the fundamentals of mathematical optimization and modeling.

## Mathematical Optimization and Modeling
<!---Imagine uses for optimization-->
Mathematical optimization (programming) systematically identifies the best solution out of a set of possible choices
with respect to a pre-specified criterion. The general form of an optimization problem is as follows:

$$
    \textrm{minimize (or maximize)} f(x) \\
    \textrm{subject to} \\
    h(x) = 0 \\
    g(x) \leq o \\
    x  \in S
$$

Where:
* $x$ is a $N$-dimensional vector referred to as, the vector of variables
* $S$ is the set from which the elements of $x$ assume values
  * For example. $S$ can be the set of real, non-negative real or non-negative integers. In general, variables in an 
    optimization problem can be continuous, discrete (integer) or combinations thereof. The former is used to
    capture the continuously varying properties of a system (e.g., concentrations), whereas the latter is used for
    discrete decision-making (e.g., whether to eliminate a reaction).
* $f(x)$ is referred to as the *objective function* and serves as a mathematical description of the desired property
    that should be optimized (i.e. maximized or minimized)