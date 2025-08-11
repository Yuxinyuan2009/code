import tensorflow as tf
import numpy as np

def solve_cubic(a, b, c, d):
    x = tf.Variable(0.0, dtype=tf.complex128)
    optimizer = tf.optimizers.Adam(learning_rate=0.01)
    for _ in range(1000):
        with tf.GradientTape() as tape:
            loss = (a * x**3 + b * x**2 + c * x + d)**2
        grads = tape.gradient(loss, [x])
        optimizer.apply_gradients(zip(grads, [x]))  
    return x.numpy()

a = 1
b = 1
c = 2
d = 3
print(solve_cubic(a, b, c, d))