n = int(input())

if 1 <= n <= 9:
print(n * n)
elif 10 <= n <= 99:
print(f"{n ** 0.5:.2f}")
elif 100 <= n <= 999:
print(f"{n ** (1/3):.2f}")
else:
print("Invalid")
