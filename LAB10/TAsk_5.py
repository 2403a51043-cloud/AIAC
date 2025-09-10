div = lambda a, b: a / b if b else "Error: Division by zero is not allowed."
print(div(10, 0), div(*(float(input("Enter value for a: ")), float(input("Enter value for b: ")))), sep='\n')
