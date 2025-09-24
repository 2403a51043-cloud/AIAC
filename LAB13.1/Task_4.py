# Ask the user to enter numbers separated by spaces
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Use list comprehension to get the squares
squares = [i * i for i in nums]

# Display the result
print("Squares:", squares)