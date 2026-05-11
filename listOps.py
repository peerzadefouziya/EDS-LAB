list1=[]
while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	n=int(input("Enter choice: "))
	if(n==1):
		N=int(input("Integer: "))
		list1.append(N)
		print("List after adding:",list1)
	elif(n==2):
		if(len(list1)==0):
			print("List is empty")
		else:
			N=int(input("Integer: "))
			if(N in list1):
				list1.remove(N)
				print("List after removing:",list1)
			else:
				print("Element not found")
	elif(n==3):
		if(len(list1)==0):
			print("List is empty")
		else:
			print(list1)
	elif(n==4):
		break
	else:
		print("Invalid choice")