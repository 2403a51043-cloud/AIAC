def add(a, b):
    """
    Add two numbers and return their sum.
    
    Args:
        a (float): The first number to be added
        b (float): The second number to be added
        
    Returns:
        float: The sum of a and b
        
    Example:
        >>> add(5, 3)
        8.0
        >>> add(2.5, 1.5)
        4.0
    """
    return a + b  # Perform addition and return the result

def subtract(a, b):
    """
    Subtract the second number from the first number and return the difference.
    
    Args:
        a (float): The number to be subtracted from (minuend)
        b (float): The number to subtract (subtrahend)
        
    Returns:
        float: The difference of a and b (a - b)
        
    Example:
        >>> subtract(10, 3)
        7.0
        >>> subtract(5.5, 2.1)
        3.4
    """
    return a - b  # Perform subtraction and return the result

def multiply(a, b):
    """
    Multiply two numbers and return their product.
    
    Args:
        a (float): The first number to be multiplied
        b (float): The second number to be multiplied
        
    Returns:
        float: The product of a and b
        
    Example:
        >>> multiply(4, 5)
        20.0
        >>> multiply(2.5, 3)
        7.5
    """
    return a * b  # Perform multiplication and return the result

def divide(a, b):
    """
    Divide the first number by the second number and return the quotient.
    
    This function handles division by zero by returning None and displaying an error message.
    
    Args:
        a (float): The dividend (number to be divided)
        b (float): The divisor (number to divide by)
        
    Returns:
        float or None: The quotient of a divided by b, or None if division by zero occurs
        
    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 0)
        Error: Division by zero is not allowed.
        None
    """
    if b == 0:  # Check if divisor is zero
        print("Error: Division by zero is not allowed.")  # Display error message
        return None  # Return None to indicate error
    return a / b  # Perform division and return the result

def main():
    """
    Main function that runs the simple calculator program.
    
    This function provides a menu-driven interface for basic arithmetic operations.
    It handles user input validation and displays results in a formatted manner.
    
    The program flow:
    1. Display calculator menu
    2. Get user's operation choice
    3. Validate the choice
    4. Get two numbers from user
    5. Perform the selected operation
    6. Display the result
    
    Note:
        The program exits gracefully if invalid input is provided.
    """
    # Display calculator title and menu options
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")        # Addition operation
    print("2. Subtract")   # Subtraction operation
    print("3. Multiply")   # Multiplication operation
    print("4. Divide")     # Division operation

    # Get user's choice for the operation
    choice = input("Enter choice (1/2/3/4): ")

    # Validate user's choice - must be one of the valid options
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice.")  # Display error message
        return  # Exit the program

    # Get two numbers from user with error handling
    try:
        num1 = float(input("Enter first number: "))  # Get first number and convert to float
        num2 = float(input("Enter second number: ")) # Get second number and convert to float
    except ValueError:  # Handle non-numeric input
        print("Invalid input. Please enter numeric values.")  # Display error message
        return  # Exit the program

    # Perform the selected operation and display result
    if choice == '1':  # Addition
        result = add(num1, num2)  # Call add function
        print(f"Result: {num1} + {num2} = {result}")  # Display addition result
    elif choice == '2':  # Subtraction
        result = subtract(num1, num2)  # Call subtract function
        print(f"Result: {num1} - {num2} = {result}")  # Display subtraction result
    elif choice == '3':  # Multiplication
        result = multiply(num1, num2)  # Call multiply function
        print(f"Result: {num1} * {num2} = {result}")  # Display multiplication result
    elif choice == '4':  # Division
        result = divide(num1, num2)  # Call divide function
        if result is not None:  # Check if division was successful (not division by zero)
            print(f"Result: {num1} / {num2} = {result}")  # Display division result

# Program entry point - only run main() when script is executed directly
if __name__ == "__main__":
    main()  # Start the calculator program
