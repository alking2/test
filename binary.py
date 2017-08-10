import cifar10
import cifar10_input
import tensorflow as tf
import numpy as np
import os
from six.moves import xrange  # pylint: disable=redefined-builtin

file = open('vtf_1.bin', 'rb')
s = file.read()
print(' '.join(map('{:02X}'.format, s)))
#print(s)

a, b = cifar10.inputs(1)
print(a)
print(type(a))
print(b)
print(type(b))
sess = tf.InteractiveSession()
init = tf.global_variables_initializer()
sess.run(init)
tf.train.start_queue_runners()
result = sess.run([a, b])
print("result")
print(result)

print("XD")


