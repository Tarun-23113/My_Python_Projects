items = ["pen", "book", "pen", "notebook", "book", "pen"]

# Count the frequency of each item using a dictionary
item_f = dict()
for item in items:
    if (item not in item_f.keys()):
        item_f.update({item:1})
    else:
        item_f[item] += 1;
print(item_f)

# Return a list of tuples sorted by frequency (descending)
sorted_dict = dict(sorted(item_f.items(), key=lambda x:x[1], reverse=True))
print(sorted_dict)

#Final Output
print(list(sorted_dict.items()))