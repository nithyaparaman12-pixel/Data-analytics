import numpy as np

print("---- NUMPY ARRAY CREATION ----")

# 1️⃣ 1D Array
arr = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr)

# 2️⃣ 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:\n", arr2)

print("\n---- ARRAY PROPERTIES ----")
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)

print("\n---- MATHEMATICAL OPERATIONS ----")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("\n---- STATISTICAL FUNCTIONS ----")
data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Min:", np.min(data))
print("Max:", np.max(data))

print("\n---- ARRAY SLICING ----")
print("Original:", arr)
print("Slice [1:4]:", arr[1:4])
print("First 3:", arr[:3])
print("Last 2:", arr[-2:])

print("\n---- ARRAY RESHAPE ----")
arr3 = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr3.reshape(2, 3)
print(reshaped)

print("\n---- SPECIAL NUMPY FUNCTIONS ----")
print("Zeros:", np.zeros(5))
print("Ones:", np.ones(3))
print("Arange:", np.arange(1, 10, 2))
print("Linspace:", np.linspace(1, 10, 5))

print("\n---- NUMPY PROGRAM COMPLETED ----")
