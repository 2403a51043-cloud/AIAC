def grade(score):
 return "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
if __name__ == "__main__":
    try:
        print(f"Grade: {grade(float(input('Enter the score: ')))}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the score.")
