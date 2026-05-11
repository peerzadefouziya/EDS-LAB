subject=int(input(""))
marks=list(map(int,input("").split()))
if any(mark<40 for mark in marks):
	print("Fail")
else:
	total_marks=sum(marks)
	Aggregate_percentage = (total_marks/(subject*100))*100
	print(f"Aggregate Percentage:{Aggregate_percentage: .2f}")
	if Aggregate_percentage > 75:
		print("Grade: Distinction")
	elif Aggregate_percentage > 60:
		print("Grade: First Division")
	elif Aggregate_percentage > 50:
		print("Grade: Second Division")
	elif Aggregate_percentage > 40:
		print("Grade: Third Division")
	else:
		print("Fail")