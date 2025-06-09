text = "Python is powerful and Python is easy to learn."

# Remove punctuation, lowercase everything
# Count word occurrences using a dictionary
# Print the 3 most frequent words

text2 = text.lower().replace('.', '').strip()
text_list = text2.split(' ')

freq = dict()
for word in text_list:
    freq[word] = freq.get(word, 0)+1;
print(freq)