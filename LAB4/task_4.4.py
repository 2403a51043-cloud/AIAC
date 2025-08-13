user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in user_input:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
