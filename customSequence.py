import numpy as np

# Take user input for the start, stop, and step of the sequence
start = int(input())
stop = int(input())
step = int(input())

# generate the sequence using np. arrange()
sequnence = np.arange(start,stop,step)
# print the generated sequnence
print(sequnence)