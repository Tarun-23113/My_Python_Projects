math = {"Alice", "Bob", "Charlie", "David"}
science = {"Charlie", "Eve", "Alice", "Frank"}

# Find students who are in both classes
print(math.intersection(science))

# Students in only one class
print(math.symmetric_difference(science))

# Students in neither (given a full class list)
print((math.union(science)).difference(math.union(science)))