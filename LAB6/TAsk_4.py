def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Ask the user for input
num = int(input("Enter a number: "))
result = sum_to_n(num)

print(f"The sum of the first {num} natural numbers is: {result}")