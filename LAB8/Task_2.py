# INSERT_YOUR_CODE
def assign_grade(score):
    # Check if score is an integer or float
    if not isinstance(score, (int, float)):
        return "Invalid input: Score must be a number."
    # Check for valid range
    if score < 0 or score > 100:
        return "Invalid input: Score must be between 0 and 100."
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

def main():
    user_input = input("Enter your marks (0-100): ")
    try:
        score = float(user_input)
        # If the user enters a float that is actually an int, convert to int for cleaner output
        if score.is_integer():
            score = int(score)
    except ValueError:
        print("Invalid input: Please enter a numeric value.")
        return
    result = assign_grade(score)
    print(f"Grade: {result}" if result in ['A', 'B', 'C', 'D', 'F'] else result)

if __name__ == "__main__":
    main()

