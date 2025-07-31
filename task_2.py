def find_highest(numbers):
    return max(numbers)

if __name__ == "__main__":
    nums = input("Enter three numbers separated by spaces: ")
    num_list = [float(n) for n in nums.split()]
    if len(num_list) != 3:
        print("Please enter exactly three numbers.")
    else:
        highest = find_highest(num_list)
        print(f"The highest value is: {highest}")