import numpy as np
import math
def f_derivative(x: float) -> float:
    return math.exp(math.sin(x) + math.cos(x)) * (math.cos(x) - math.sin(x))
print(f_derivative(2))