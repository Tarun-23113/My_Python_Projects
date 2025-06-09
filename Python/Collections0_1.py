data = ["  apple", "Banana ", "APPLE", "banana", "Orange", " orange "]
print(data)

# ✅ Task:
# Normalize all strings (strip, lowercase)
# Remove duplicates
# Return a sorted list of unique items

# data2 = [ data[i].lower().strip() for i in range(len(data))]
# data2_set = set(data2)
# data_cleaned = sorted(list(data2_set))

# print(data_cleaned)

#Better Way by ChatGPT

data_cleaned = sorted(list(set(data[i].lower().strip() for i in range(len(data)))))
print(data_cleaned)