import numpy as np
import tensorflow as tf
f = open("vtf_1.bin", "r")
a = np.fromfile(f, dtype=np.float32)
print(a[387200:387250])

f = open("vtf_2.bin", "r")
b = np.fromfile(f, dtype=np.float32)
print(b[0:100])
