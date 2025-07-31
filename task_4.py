num_students = int(input("Enter the number of students: "))

students = []
for i in range(num_students):
    print(f"\nEnter details for student {i+1}:")
    name = input("Name: ")
    roll_no = input("Roll No: ")
    marks = input("Marks: ")
    students.append({'Name': name, 'Roll No': roll_no, 'Marks': marks})

print("\nStudent Details:")
print("{:<20} {:<15} {:<10}".format("Name", "Roll No", "Marks"))
print("-" * 45)
for student in students:
    print("{:<20} {:<15} {:<10}".format(student['Name'], student['Roll No'], student['Marks']))