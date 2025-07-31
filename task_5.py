input_str = input("Enter a string: ")
words = input_str.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(f"'{word}': {count}")