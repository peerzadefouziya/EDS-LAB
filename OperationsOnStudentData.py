import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)

# 1. Print all student details
print("All student Details:\n", a)

# 2. print total students

print("Total Students:", int(a.shape[0]))

# 3. Print all student Roll numbers
print("All Student Roll Nos",a[:,0])
# 4. Print subject 1 marks
print("Subject 1 Marks", a[:,1])

# 5. print minimum marks of Subject 2
print("Min marks in Subject 2",np.min(a[:,2]))

# 6. print maximum marks of Subject 3
print("Max marks in Subject 3",np.max(a[:,3]))

# 7. Print All subject marks
print("All subject marks:",a[:,1:])

# 8. print Total marks of students
print("Total Marks",np.sum(a[:, 1:], axis=1))

# 9. print average marks of each student
print(np.round(np.mean(a[:, 1:], axis=1), 1))

# 10. print average marks of each subject
print("Average Marks of each subject", np.mean(a[:, 1:], axis=0))

# 11. print average marks of S1 and S2
print("Average Marks of S1 and S2", np.mean(a[:, 1:3], axis=0))

# 12. print average marks of S1 and S3
print("Average Marks of S1 and S3", np.mean(a[:, [1, 3]], axis=0))

# 13. print Roll number who got maximum marks in Subject 3
max_s3_index = np.argmax(a[:, 3])
print("Roll no who got maximum marks in Subject 3", a[max_s3_index, 0])

# 14. print Roll number who got minimum marks in Subject 2
min_s2_index = np.argmin(a[:, 2])
print("Roll no who got minimum marks in Subject 2", a[min_s2_index, 0])

# 15. print Roll number who got 24 marks in Subject 2
roll_24 = a[a[:, 2] == 24][:, [0]]
print("Roll no who got 24 marks in Subject 2", roll_24)

# 16. print count of students who got marks in Subject 1 < 40
count_s1_less_40 = np.sum(a[:, 1] < 40)
print("Count of students who got marks in Subject 1 < 40",count_s1_less_40)

# 17. print count of students who got marks in Subject 2 > 90
count_s2_more_90 = np.count_nonzero(a[:, 2] > 90)
print(f"Count of students who got marks in Subject 2 > 90: {count_s2_more_90}")

# 18. print count of students in each subject who got marks >= 90
count_each_sub_90 = np.sum(a[:, 1:] >= 90, axis=0)
print("Count of students in each subject who got marks >= 90:",count_each_sub_90)

# 19. print count of subjects in which each student got marks >= 90
print("Roll no:", a[:, 0])
count_stud_sub_90 = np.sum(a[:, 1:] >= 90, axis=1)
print("Count of subjects in which student got marks >= 90:",count_stud_sub_90)

# 20. Print S1 marks in ascending order
print(np.sort(a[:, 1]))
# 21. Print S1 marks >= 50 and <= 90
students_50_90 = a[(a[:, 1] >= 50) & (a[:, 1] <= 90)]
print(students_50_90)
print(a)

# 22. Print the index position of marks 79
indices_79 = np.where(a[:, 1] == 79)
print(indices_79)

