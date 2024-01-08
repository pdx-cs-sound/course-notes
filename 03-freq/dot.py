import numpy as np

def dot(a, b):
    assert len(a) == len(b)
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i]
    return sum

def np_dot(a, b):
    assert len(a) == len(b)
    return a.dot(b)

a = np.array([1, 7, 3], dtype=np.float32)
b = np.array([-1, 2, -1], dtype=np.float32)

print(dot(a, b))
print(np_dot(a, b))
