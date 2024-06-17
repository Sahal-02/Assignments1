import numpy as np

# initializing string
test_str = "GeeksforGeeks"

# using numpy to get count of each element in string
unique, counts = np.unique(np.array(list(test_str)), return_counts=True)
all_freq = dict(zip(unique, counts))

# printing result
print("Count of all characters in GeeksforGeeks is :\n " + str(all_freq))
#This code is contributed by Jyothi pinjala
