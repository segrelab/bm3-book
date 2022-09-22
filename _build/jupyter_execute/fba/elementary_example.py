#!/usr/bin/env python
# coding: utf-8

# # FBA from Scratch: Elementary Example

# This example is from Bonarius et al., "Flux analysis of underdetermined metabolic networks: the quest for the missing constraints", Trends in Biotechnology 1997,
# https://www.cell.com/trends/biotechnology/fulltext/S0167-7799(97)01067-6
# 
# (Note: this part also contains some general purpose functions for visualization of FBA data)

# ## Import Libraries
# 
# Import essential libraries, including basic numerical and graphics library and scipy optimization library.

# In[1]:


import numpy as np # Imports Python numerical library
import seaborn as sns # Imports Library for drawing heatmaps
import matplotlib.pyplot as plt # Import Library for plotting graphs
from scipy.optimize import linprog # Imports Linear Programming function
from scipy.optimize import linprog_verbose_callback # Imports Linear Programming function


# ## Define reaction network
# Define reaction network, i.e. stoichiometric matrix and labels of metabolites and reactions

# In[ ]:


# Labels of reactions:
reacs =["x1","x2","ra","rb","ATPout","NADHout"]
# Labels of metabolites:
metabs = ["A","B","ATP","NADH"]

n = len(reacs) # Number of reactions
m = len(metabs) # Number of metabolites

# Define values of Stoichiometric Matrix
S=np.array([[ -1, -1,  1,  0,  0,  0],
            [  1,  1,  0, -1,  0,  0],
            [  1,  0,  0,  0, -1,  0],
            [  0,  1,  0,  0,  0, -1]])

print("STOICHIOMETRIC MATRIX")
colormap = sns.color_palette("Greens")
sns.heatmap(S, annot=True,  linewidths=.5, xticklabels=reacs,yticklabels=metabs,cmap="PiYG")
plt.yticks(rotation=0)
plt.show()


# ### Define optimization parameters
# 
# Define optimization parameters, i.e. flux lower bounds (LB) and upper bounds (UB), and objective function.

# In[ ]:


b=np.zeros(m) # Right-hand side of SV=0
obj=np.zeros(n) # Initialize Objective function vector to zero
LARGE = 1000 # Large number to be used as "Infinite" for flux bounds
LB=0*np.ones(n) # Set of lower bounds, initialize to zero
UB=LARGE*np.ones(n) # Set of upper bounds, initialize to LARGW

# Change flow through individual reaction
UB[2]=1

LBUB = np.transpose(np.stack((LB,UB),axis=0)) # Combine LB, UB into set of pairs [LB,UB]

obj[0]=-1 # Define objective function. Default of optimizer is "minimize", so a -1 will lead to maximization
obj[1]=0 # Define objective function. Default of optimizer is "minimize", so a -1 will lead to maximization


# ## Run LP to solve FBA
# 
# Perform Linear Programming (LP) calculation to solve FBA

# In[ ]:


print("IMPLEMENT OPTIMIZATION:")
options = {"disp": False}
solution = linprog(c=obj, A_eq=S, b_eq=b, bounds=LBUB, options=options) # max c*v, given Sv=b, LB < v <UB
#print(solution)
# A_eq*v=b_eq --> SV=0

print("Optimization status (0:successful; 1:Iteration limit reached; 2:Infeasible; 3:Unbounded; 4:Numerical difficulties): ",solution.status)
print("Optimal value: ",solution.fun)
print("Solution vector: ", solution.x)


# ## Display solution
# Visualize solution vector

# In[ ]:


v_pos = np.arange(n)
plt.bar(v_pos, solution.x, align='center')
plt.xticks(v_pos, reacs)
plt.ylabel('Flux Value')
plt.title('Solution Vector')
plt.show()


# Display list of reactions and associated fluxes

# In[ ]:


# TODO: import this function from GEM-utils
pretty_print_fluxes(S,reacs,metabs,solution)


# ## Draw network with fluxes
# 
# Define function for drawing graph of metabolic network, with arrow thickness proportional to fluxes

# In[ ]:


draw_network(S,reacs,metabs,solution)


# ## Questions
# 
# 1. What would happen in absence of the "ATP out" and "NADH out" reactions?
# 2. What geometrical entity represents the feasible space for this problem?

# 

# 
