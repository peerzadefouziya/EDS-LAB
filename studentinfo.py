import pandas as pd

file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])

print("First five rows:")
print(data.head())
avg = round(data["Age"].mean(),2)
print("Average age:", avg)
filter = data[data["Grade"] <= "B"]
print("Students with a grade up to B")
print (filter)
