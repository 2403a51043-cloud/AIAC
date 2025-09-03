# INSERT_YOUR_CODE
def is_sentence_palindrome(sentence):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in sentence if c.isalnum())
    return cleaned == cleaned[::-1]

def main():
    user_input = input("Enter a sentence: ")
    if is_sentence_palindrome(user_input):
        print("The sentence is a palindrome.")
    else:
        print("The sentence is not a palindrome.")

if __name__ == "__main__":
    main()
