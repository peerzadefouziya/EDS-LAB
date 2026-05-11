# Reverse a Number

# Taking input
num = int(input())

# Intialize reversed number
rev = 0

# Loop to reverse digits
while num > 0:
	digit = num % 10     # get last digit
	rev = rev * 10 + digit
	num = num // 10      # remove last digit

# Print result
print(rev)