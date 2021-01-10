import numpy as np

print(np.zeros(3))
print(np.ones(3))
print(np.empty(3))
array_full = np.full(3, 7.0)
print(array_full, array_full.dtype)
arange_array = np.arange(-5, 5)
print(arange_array[arange_array > 3])
print(arange_array[arange_array < 1])