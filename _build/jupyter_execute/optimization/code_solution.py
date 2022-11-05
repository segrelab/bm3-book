#!/usr/bin/env python
# coding: utf-8

# # Simplex Algorithm from Scratch in Python

# In[1]:


import math
import numpy as np


# The algorithm itself will consist of these steps:
# 1. Convert equational form to the tableau.
# 2. Until we reached the solution find pivot position and make pivot step.
# 3. Convert tableau to the solution of the linear program.

# In[4]:


def simplex(c, A, b):
    tableau = to_tableau(c, A, b)

    while can_be_improved(tableau):
        pivot_position = get_pivot_position(tableau)
        tableau = pivot_step(tableau, pivot_position)

    return get_solution(tableau)


# Tableau in the algorithm will contain all the information about the linear program, therefore, it will look different from what we had on paper. We will use this function to convert the equational form to the tableau.

# In[5]:


def to_tableau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    return xb + [z]


# In the next function, we check where nonbasic values can be increased without making the objective function value smaller.

# In[6]:


def can_be_improved(tableau):
    z = tableau[-1]
    return any(x > 0 for x in z[:-1])


# If the value of an objective function can be improved we search for a pivot position.

# In[7]:


def get_pivot_position(tableau):
    z = tableau[-1]
    column = next(i for i, x in enumerate(z[:-1]) if x > 0)
    
    restrictions = []
    for eq in tableau[:-1]:
        el = eq[column]
        restrictions.append(math.inf if el <= 0 else eq[-1] / el)

    row = restrictions.index(min(restrictions))
    return row, column


# Next, we call function that will make pivot step and return new tableau.

# In[8]:


def pivot_step(tableau, pivot_position):
    new_tableau = [[] for eq in tableau]
    
    i, j = pivot_position
    pivot_value = tableau[i][j]
    new_tableau[i] = np.array(tableau[i]) / pivot_value
    
    for eq_i, eq in enumerate(tableau):
        if eq_i != i:
            multiplier = np.array(new_tableau[i]) * tableau[eq_i][j]
            new_tableau[eq_i] = np.array(tableau[eq_i]) - multiplier
   
    return new_tableau


# The final step in our algorithm is to extract the solution vector from the tableau. In the picture, we can see that columns where there is only one element equal to one and all other to zero have the same index as a basic variable in the right-hand tableau example.

# In[9]:


def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

def get_solution(tableau):
    columns = np.array(tableau).T
    solutions = []
    for column in columns[:-1]:
        solution = 0
        if is_basic(column):
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)
        
    return solutions


# Now, let’s run the algorithm.

# We will pass to the algorithm linear program in equational representation that looks like this.

# In[ ]:


c = [1, 1, 0, 0, 0]
A = [
    [-1, 1, 1, 0, 0],
    [ 1, 0, 0, 1, 0],
    [ 0, 1, 0, 0, 1]
]
b = [2, 4, 4]


# In[10]:


solution = simplex(c, A, b)
print('solution: ', solution)

