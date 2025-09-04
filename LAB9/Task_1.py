def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers from a given list.
    
    This function iterates through a list of numbers and separates them into
    even and odd categories, then calculates the sum for each category.
    
    Args:
        numbers (list): A list of integers to be processed.
        
    Returns:
        tuple: A tuple containing two integers:
            - First element: sum of all even numbers in the list
            - Second element: sum of all odd numbers in the list
            
    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5, 6])
        (12, 9)
        >>> sum_even_odd([10, 15, 20, 25])
        (30, 40)
        
    Note:
        - Numbers are considered even if they are divisible by 2 (num % 2 == 0)
        - All other numbers are considered odd
        - If the input list is empty, returns (0, 0)
    """
    even_sum = 0  # Initialize counter for sum of even numbers
    odd_sum = 0   # Initialize counter for sum of odd numbers
    
    # Iterate through each number in the input list
    for num in numbers:
        if num % 2 == 0:  # Check if number is even (divisible by 2)
            even_sum += num  # Add even number to even sum
        else:  # Number is odd
            odd_sum += num   # Add odd number to odd sum
    
    return even_sum, odd_sum  # Return tuple with both sums

# Get user input as a string of numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Convert input string to list of integers
# strip() removes leading/trailing whitespace, split() creates list of strings, int() converts to integers
num_list = [int(x) for x in user_input.strip().split()]

# Call the function to calculate sums and unpack the returned tuple
even_sum, odd_sum = sum_even_odd(num_list)

# Display the results to the user
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
"""
This script prompts the user to enter a list of numbers separated by spaces,
then calculates and prints the sum of even and odd numbers separately.

Functions:
    sum_even_odd(numbers): Takes a list of integers and returns a tuple containing
    the sum of even numbers and the sum of odd numbers."""

