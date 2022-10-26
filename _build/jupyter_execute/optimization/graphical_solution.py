#!/usr/bin/env python
# coding: utf-8

# # Graphical Solution

# ## Some algebra review
# <!-- TODO: Change to a note box -->
# Suppose you have two constraints as follows:
# 2x1 + 3x2 ≤ 34
# 3x1 + 5x2 ≤ 54
# Also assume that x1 and x2 are objects and must be ≥ 0.
# You can graph these inequalities…

# ## Graphical Optimization
# The overlap of these graphs is known as the feasible region. A solution to the problem must lie in the region in order to obey both of the constraints. 
# <!-- TODO: insert image -->

# And, because the constraints are linear, the maximum and minimum must lie on the boundary.
# <!-- TODO: insert image -->

# In fact, it is most likely that the optimum occurs at one of the corner points. 
# We can even find the values of the corner points with a little algebra…
# <!-- TODO: Work math on an example -->
# Point out that the inequalities dropped away because we’re focusing on the boundary.
# 
# ## Practice problem
# Suppose a company hires both experienced and inexperienced workers. 
# Experienced workers are paid $15/hour and inexperienced workers are paid $10/hour. The company can spend $1200/hour on labor.
# Experienced workers require an average of 1 minute an hour of contact with a supervisor; inexperienced workers require 2. There are two supervisors who can provide 120 minutes in an hour.
# 2. Convert both of these into inequality constraints. Graph them, find the feasible region, and find all four corner points.
# 
# <!-- The constraints are:
# 15x1 + 10x2 ≤ 1200
# 1x1 + 2x2 ≤ 120
# 
# The graph is a typical quadrilateral; corner points are at (0, 0), (80, 0), (0, 60) and (60, 30).
# -->
# 
# 
# ## Enter the Objective Function
# After you have the feasible region and the corner points, it’s time to consider the objective function. 
# 
# A way to find the optimum without plugging in points is to sketch the slope of the objective function on the graph.
# If you drag the slope line to the
# right, you can see that the last 
# place it touches the feasible region is (17, 0). This will be the best point.

# In[1]:


import plotly.graph_objects as go
import numpy as np

# Create figure
fig = go.Figure()

# Plot the inequality 2x + 3y <= 25
x = np.linspace(0, 13, 50)
y = (25 - 2*x)/3
fig.add_trace(go.Scatter(x=x, y=y, mode='none', name='2x + 3y <= 25', fill='tozeroy'))

# Plot the inequality 6x + 3y <= 45
y = (45 - 6*x)/3
fig.add_trace(go.Scatter(x=x, y=y, mode='none', name='6x + 3y <= 45', fill='tozeroy'))

# Add traces, one for each slider step
for step in np.arange(0, 100, 1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=6),
            name="𝜈 = " + str(step),
            y=(step - 7*x)/8
            )
        )

# # Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Slack variable: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.update_yaxes(
    range=(0, 15),
    constrain='domain'
)

fig.show()


# Another way to optimize is to find the value of the objective function by plugging in each point, then choose the best one.
# <!-- TODO: Values for an example -->
# 
# ## Practice Problem
# Write and optimize each objective function using your graph and points from problem 2. First plug in all the points to find the maximum, then use the slope of the objective function to verify your answer.
# 3a. The company finds that experienced workers complete 10 tasks per minute, while inexperienced workers only complete 9. Maximize task completion.
# 3b. The company finds that experienced workers make higher quality products, generating 3 new customers per worker per year. Inexperienced workers generate 2. Maximize customer gain. 
# <!-- The corner points were (0, 0), (0, 60), (80, 0) and (30, 60).
# 3a. f = 10x1 + 9x2; maximized at (30, 60) with f = 840. The company should hire 30 experienced and 60 inexperienced workers for 840 tasks per minute.
# 3b. f = 3x1 + 2x2; maximized at (80, 0) with f = 240. The company should hire 80 experienced and 0 inexperienced workers for 240 customers per year.
# 
# Encourage students to write, or at least think about, the meaning of the points rather than just the numerical values. 
# -->
# 
# ## Active and Inactive Constraints
# An optimal solution that lies at the intersection point of two constraints causes both of those constraints to be considered active. 
# <!-- TODO: Insert image -->
# 
# If any of the constraint lines do not pass through the optimal point, those constraints are called inactive.
# 
# In general, we ignore the constraints at 0 and focus on the constraints generated by limits on resources. 
# An active constraint means that this factor is causing the limitation on the objective function. If an active constraint was amount of flour, then by increasing the flour available you could improve your objective. If all your constraints are active, that is good news – you are using all your resources.
# An inactive constraint means that this factor is not causing the limitation. If amount of flour was an inactive constraint, then you will have flour left over; perhaps you could use it for something else or sell it. 
# 
