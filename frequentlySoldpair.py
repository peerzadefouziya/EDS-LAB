import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)
group=df.groupby("Date")["Product"].apply(list)
counter=Counter()
for product in group :
	pairs=combinations(sorted(product),2)
	counter.update(pairs)
	max_frequency=max(counter.values())
	most_common_pairs=[(pair,freq)for pair,freq in counter.items()if freq==max_frequency]

for(product1,product2), frequency in most_common_pairs:
	print(f"{product1} and {product2}: {frequency} times")