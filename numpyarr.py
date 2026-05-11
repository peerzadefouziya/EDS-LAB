import numpy as np  


r, c = map(int, input().split())

elements=[]

for i in range (r):
	row= list(map(int,input().split()))
	elements.extend(row)

arr = np.array(elements)
arr = arr.reshape(r,c)

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)