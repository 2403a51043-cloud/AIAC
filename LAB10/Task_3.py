n = input("Enter employee name: ")
s = float(input("Enter employee salary: "))
p = float(input("Enter increment percentage: "))
s += s * p / 100
print("emp:", n, "salary:", s)
