students = {
    "A101": {"name": "Alice", "marks": {"math": 88, "science": 92}},
    "B202": {"name": "Bob", "marks": {"math": 75, "science": 85}},
}

# Print names of students scoring > 80 in both subjects
for report in students.values():
    if (report["marks"]["math"]>80 and report["marks"]["science"]>80):
        print(report["name"])
    else:
        continue

# Calculate average marks per subject across students
total_math = 0
total_science = 0
count = 0
for value in students.values():
    count += 1
    total_math += value['marks']['math']
    total_science += value['marks']['science']

print(f"Average Marks in Math {total_math/count}")
print(f"Average Marks in Science {total_science/count}")