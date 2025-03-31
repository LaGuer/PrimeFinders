import numpy as np
from scipy.integrate import quad
from scipy.constants import pi, euler_gamma

# Define the logarithmic function
def log2_function(x):
    return np.log2(x)

# Modified T(x) function
def T(x):
    # Apply a transformation to x (e.g., x + x^2 or another variation)
    return np.log(x) + x**2  # Example transformation

# Define parameters for variation
parameters = [
    {"start": 1, "end": 100, "factor": 2},
    {"start": 1, "end": 200, "factor": 3},
    {"start": 50, "end": 150, "factor": 1.5},
]

# Simulate for each set of parameters
for param in parameters:
    start = param["start"]
    end = param["end"]
    factor = param["factor"]
    
    # Simulate j values in the specified range
    for j in range(start, end + 1):
        # Calculate the integrals
        integral1, _ = quad(log2_function, j, j + 1)
        integral2, _ = quad(log2_function, 1 / (j + 1), 1 / j)
        
        # Scale the sum of integrals by the factor
        scaled_sum = factor * (integral1 + integral2)
        
        # Calculate Ж and Ч
        Ж = T(pi)
        Ч = T(euler_gamma)
        
        # Ensure the proportionality condition is met
        ratio1 = Ч / euler_gamma
        ratio2 = Ж / pi
        
        # Print results for each simulation
        print(f"j: {j}, Factor: {factor}")
        print(f"Integral 1: {integral1}")
        print(f"Integral 2: {integral2}")
        print(f"Scaled Sum of Integrals: {scaled_sum}")
        print(f"Ж: {Ж}")
        print(f"Ч: {Ч}")
        print(f"Ratio Ч/γ: {ratio1}")
        print(f"Ratio Ж/π: {ratio2}")
        print(f"Proportionality verified: {np.isclose(ratio1, ratio2)}")
        print("-" * 50)
