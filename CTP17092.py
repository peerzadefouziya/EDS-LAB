data=input().split(" ")
e=input()
found=False
for i,j in enumerate(data):
	if j==e:
		print(i)
		found=True
		break
if not found:
	print("Not found")