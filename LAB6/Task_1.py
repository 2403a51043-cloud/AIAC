class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        def display_details(self):
        print("\n--- Student Details ---")
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Marks    : {self.marks}")
        def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"
num_students = int(input("Enter the total number of students: "))
students = []
for i in range(num_students):
    print(f"\nEnter details for student {i+1}:")
    name = input("Name: ")
    roll_no = input("Roll No: ")
    marks = float(input("Marks: "))
    student = Student(name, roll_no, marks)
    students.append(student)
for student in students:
    student.display_details()
    print(f"Grade    : {student.calculate_grade()}")
    print("-" * 35)
    print(f"{'Name':<15}{'Roll No':<10}{'Marks':<7}{'Grade':<6}")
    print("-" * 35)
    for s in students:
        print(f"{s.name:<15}{s.roll_no:<10}{s.marks:<7}{s.calculate_grade():<6}")
    print("-" * 35)
                