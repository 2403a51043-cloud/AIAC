def print_students(students):
    print("\nStudent List:")
    for student in students:
        print(student)

# List to store student names
students = []

while True:
    name = input("Enter student name (or press Enter to finish): ")
    if name == "":
        break
    students.append(name)

# Call the function to print the students
print_students(students)
