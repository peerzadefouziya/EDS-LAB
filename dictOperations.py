# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

print("Original Dictionary:",student)
key=int(input())
value=input()
student[key]=value
print("After Insertion:",student)
key=int(input())
value=input()
student[key]=value
print("After Update:",student)
key=int(input())
student.pop(key,None)

print("After Deletion:",student)
print("Traversing Dictionary:")
for i in student:
	print(f"{i} : {student.get(i)}")