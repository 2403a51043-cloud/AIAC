items = [10, 20, 30, 40, 50]
num = int(input("Enter a number to search: "))
found = num in items
if found:
    print(f"\n{num} is found in the list.\n")
else:
    print(f"\n{num} is not found in the list.\n")