import numpy as np
from scipy.integrate import quad
import mpmath

# Define the integral function with variations
def integral_term(j, precision="normal", base=2, adjust_limits=False):
    if precision == "high":
        # Use higher precision with mpmath for integration
        with mpmath.workdps(50):  # Set desired decimal places for high precision
            result = mpmath.quad(lambda x: mpmath.log(x, base), [1/j if not adjust_limits else 1/(j+1), j if not adjust_limits else (j-0.5)])
    else:
        # Use standard precision
        result, _ = quad(lambda x: np.log(x)/np.log(base), 1/j if not adjust_limits else 1/(j+1), j if not adjust_limits else (j-0.5))
    return result

# Compute the summation for a finite n
def compute_sum(n, precision="normal", base=2, adjust_limits=False):
    summation = 0
    for j in range(1, n + 1):
        summation += 2**(-j) * (1 - integral_term(j, precision, base, adjust_limits))
    return summation

# Test the function with different variations
n = 10000  # Large value for convergence

# Variation 1: Standard precision, no adjustments
result_standard = 2 * compute_sum(n, precision="normal", base=2, adjust_limits=False)
print("Standard Precision Result:", result_standard)

# Variation 2: High precision using mpmath
result_high_precision = 2 * compute_sum(n, precision="high", base=2, adjust_limits=False)
print("High Precision Result:", result_high_precision)

# Variation 3: Adjusted integration limits
result_adjusted_limits = 2 * compute_sum(n, precision="normal", base=2, adjust_limits=True)
print("Adjusted Limits Result:", result_adjusted_limits)

# Variation 4: Alternative logarithm base
alternative_base = np.e  # Natural logarithm
result_alternative_base = 2 * compute_sum(n, precision="normal", base=alternative_base, adjust_limits=False)
print(f"Result with Base {alternative_base}:", result_alternative_base)
