import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Array:", arr)

print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

print("First 5 elements:", arr[:5])

arr[-3:] = [100, 200, 300]
print("Modified array:", arr)

print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())