data = [
  {"name": "Alice", "score": 90},
  {"name": "Bob", "score": 85},
  {"name": "Alice", "score": 95},
]

# List of Dict to Dict of Lists

new_dict = dict()

for item in data:
    new_dict[item['name']] = new_dict.get(item['name'], 0)+item['score']

print(new_dict)