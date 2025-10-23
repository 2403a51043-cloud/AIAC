def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)


# Ask the user to enter a number
num = int(input("Input: "))

# Calculate factorial
result = factorial(num)

# Display output in required format
print("Output: Factorial =", result)
