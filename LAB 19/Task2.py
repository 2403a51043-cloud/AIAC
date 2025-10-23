def check_number(num):
    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is zero")


# Asking user for inputs
num1 = int(input("Enter a number: "))
check_number(num1)

num2 = int(input("Enter another number: "))
check_number(num2)

num3 = int(input("Enter one more number: "))
check_number(num3)
