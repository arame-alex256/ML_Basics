import numpy as np

a = np.array([2, 3])
b = np.array([4, 1])

# Addition 2+4 3+1
print(a + b)

# Scalar multiplication 3*2 3*3
print(3 * a)

# Magnitude 2^2 + 3^2 = 13
print(np.linalg.norm(a))

# Dot product 2*4 + 3*1 = 11
print(np.dot(a, b))

c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])

print(f"Matrix c: {c}")
print(f"Matrix d: {d}")

# Matrix multiplication
print(f"Matrix multiplication: {np.dot(c, d)}")
# Matrix addition
print(f"Matrix addition: {c + d}")
# Matrix subtraction
print(f"Matrix subtraction: {c - d}")
# Matrix multiplication
print(f"Matrix multiplication: {c * d}")
# Matrix division
print(f"Matrix division: {c / d}")
# Matrix power
print(f"Matrix power: {c ** 2}")
# Matrix Magnitude
print(f"Matrix Magnitude: {np.linalg.norm(c)}")