import re

# task2.py
# Ask the user for numbers and use a list comprehension to filter even numbers.


def parse_numbers(s):
    parts = re.split(r'[,\s]+', s.strip())
    nums = []
    for p in parts:
        if p == '':
            continue
        try:
            nums.append(int(p))
        except ValueError:
            print(f"Ignoring invalid token: {p!r}")
    return nums

def main():
    s = input("Enter numbers separated by spaces or commas: ")
    numbers = parse_numbers(s)
    # List comprehension to filter even numbers
    evens = [n for n in numbers if n % 2 == 0]
    if evens:
        print("Even numbers:", evens)
    else:
        print("No even numbers found.")

if __name__ == "__main__":
    main()