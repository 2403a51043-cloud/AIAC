def generate_student_mail_ids():
    n = int(input("Enter the number of students: "))
    mail_ids = []
    for i in range(n):
        first_name = input(f"Enter first name of student {i+1}: ").strip().lower()
        last_name = input(f"Enter last name of student {i+1}: ").strip().lower()
        mail_id = f"{first_name}{last_name}@sru.edu.in"
        mail_ids.append(mail_id)
    print("Generated student mail ids:")
    for mail in mail_ids:
        print(mail)

if __name__ == "__main__":
    generate_student_mail_ids()
