# Ask the user to input words separated by spaces
user_input = input("Enter words separated by spaces: ")
words = user_input.split()

# Build the sentence using join for efficiency
sentence = " ".join(words)

# Display the result
print(sentence)