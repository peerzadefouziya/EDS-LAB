from datetime import datetime

# Read input dates
date1 = input().strip()
date2 = input().strip()

# Convert string to date object
d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

# Calculate difference
diff = (d2- d1).days

# Print result
print(diff)