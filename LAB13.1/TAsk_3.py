class Student:
    """
    Represents a student with a name, age, and a list of marks.
    """

    def __init__(self, name, age, marks):
        """
        Initialize a Student instance.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            marks (list of int): The student's marks.
        """
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        """
        Prints the student's name and age in a readable format.
        """
        print(f"Student Details:\n  Name: {self.name}\n  Age: {self.age}")

    def total_marks(self):
        """
        Returns the total of the student's marks.

        Returns:
            int: The sum of all marks.
        """
        return sum(self.marks)


# Get user input and display result
if __name__ == "__main__":
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = []
    for i in range(1, 4):
        mark = int(input(f"Enter mark {i}: "))
        marks.append(mark)

    student = Student(name, age, marks)
    student.display_details()
    print(f"Total Marks: {student.total_marks()}")