age = int(input("Enter your age: "))

if age >= 0:
    if age < 2:
        print("Infant")
    elif age < 13:
        print("Child")
    elif age < 20:
        print("Teenager")
    elif age < 60:
        print("Adult")
    else:
        print("Senior")
else:
    print("Invalid age entered.")