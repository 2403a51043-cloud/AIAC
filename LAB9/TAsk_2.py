class sru_student:
    """
    A class to represent a student at SRU (Shri Ramswaroop Memorial University).
    
    This class manages student information including personal details, hostel status,
    and fee payment status. It provides methods to update fee status and display
    student information.
    
    Attributes:
        name (str): The student's full name
        roll_no (str): The student's unique roll number
        hostel_status (str): Whether the student lives in hostel (Yes/No)
        fee_paid (bool): Whether the student has paid their fees (default: False)
    
    Methods:
        __init__(name, roll_no, hostel_status): Initialize a new student object
        fee_update(status): Update the fee payment status
        display_details(): Print all student information
    
    Example:
        >>> student = sru_student("John Doe", "2023001", "Yes")
        >>> student.fee_update(True)
        >>> student.display_details()
    """
    
    def __init__(self, name, roll_no, hostel_status):
        """
        Initialize a new SRU student object.
        
        Args:
            name (str): The student's full name
            roll_no (str): The student's unique roll number
            hostel_status (str): Whether the student lives in hostel (Yes/No)
        """
        self.name = name  # Store student's name
        self.roll_no = roll_no  # Store student's roll number
        self.hostel_status = hostel_status  # Store hostel accommodation status
        self.fee_paid = False  # Initialize fee status as unpaid

    def fee_update(self, status):
        """
        Update the fee payment status of the student.
        
        Args:
            status (bool): True if fee is paid, False if unpaid
            
        Note:
            Only boolean values are accepted. Other types will result in an error message.
        """
        if isinstance(status, bool):  # Check if input is a boolean value
            self.fee_paid = status  # Update fee status
        else:  # If input is not boolean
            print("Invalid status. Please provide True or False.")  # Display error message

    def display_details(self):
        """
        Display all student information in a formatted manner.
        
        Prints the student's name, roll number, hostel status, and fee payment status.
        The fee status is converted from boolean to "Yes"/"No" for better readability.
        """
        print("Student Details:")  # Print header
        print(f"Name: {self.name}")  # Display student's name
        print(f"Roll No.: {self.roll_no}")  # Display roll number
        print(f"Hostel Status: {self.hostel_status}")  # Display hostel status
        # Convert boolean fee status to "Yes"/"No" for display
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")

# Main program execution
# Ask user for input to create a new student object
name = input("Enter student name: ")  # Get student's name from user
roll_no = input("Enter roll number: ")  # Get student's roll number from user
hostel_status = input("Enter hostel status (Yes/No): ")  # Get hostel status from user

# Create a new student object with the provided information
student = sru_student(name, roll_no, hostel_status)

# Ask user about fee payment status
fee_input = input("Has the fee been paid? (Yes/No): ")
# Check if user input is "yes" (case-insensitive) and update fee status accordingly
if fee_input.strip().lower() == 'yes':  # strip() removes whitespace, lower() makes case-insensitive
    student.fee_update(True)  # Set fee status to paid
else:  # If input is anything other than "yes"
    student.fee_update(False)  # Set fee status to unpaid

# Display student details for the first time
student.display_details()
print("\nDisplaying student details again:")  # Print separator message
student.display_details()  # Display student details again
