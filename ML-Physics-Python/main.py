import torch
import math

# Define the equation to be approximated
def range_equation(y0, v0, t, theta):
    # Corrected mathematical expression with proper operators and function calls
    return y0 + v0 * t * math.sin(theta) - (1/2) * 9.8 * t**2
