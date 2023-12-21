"""
In this code:
We define an example quadratic objective function f(x) = x^2 and its gradient f'(x) = 2x.
The gradient_descent function performs the gradient descent optimization with the given learning rate and number of iterations.
We store the history of x values during each iteration to track the trajectory.
The code then plots the objective function and the trajectory of x values.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the objective function
def objective_function(x):
    return x**2

# Define the gradient of the objective function
def gradient(x):
    return 2 * x

# Gradient Descent function
def gradient_descent(learning_rate, iterations):
    x = 10  # Initial guess
    history = []  # To store the history of x values for plotting

    for _ in range(iterations):
        history.append(x)
        x = x - learning_rate * gradient(x)

    return history

# Set hyperparameters
learning_rate = 0.1
iterations = 20

# Run gradient descent
trajectory = gradient_descent(learning_rate, iterations)

# Plot the objective function and the trajectory
x = np.linspace(-12, 12, 400)
y = objective_function(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Objective Function')
plt.plot(trajectory, [objective_function(x) for x in trajectory], 'ro-', label='Trajectory')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent')
plt.legend()
plt.grid(True)
plt.show()