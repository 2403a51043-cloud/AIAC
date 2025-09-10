def find_common(a,b):
    return list(set(a) & set(b))

a = input("Enter the first list of values separated by spaces: ").split()
b = input("Enter the second list of values separated by spaces: ").split()
common = find_common(a, b)
print("Common elements:", common)

