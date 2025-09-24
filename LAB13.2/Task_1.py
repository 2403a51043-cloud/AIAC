# Ask the user to enter numbers separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# Use list comprehension to compute squares
squares = [n ** 2 for n in numbers]
print(squares)