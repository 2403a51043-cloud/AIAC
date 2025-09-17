import random
import time

def get_student_records():
    n = int(input("Enter the number of students: "))
    students = []
    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        name = input("Name: ")
        roll = input("Roll No: ")
        while True:
            try:
                cgpa = float(input("CGPA: "))
                break
            except ValueError:
                print("Invalid CGPA. Please enter a number.")
        students.append({'Name': name, 'Roll': roll, 'CGPA': cgpa})
    return students

# Quick Sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[random.randint(0, len(arr)-1)]['CGPA']
        left = [x for x in arr if x['CGPA'] > pivot]
        middle = [x for x in arr if x['CGPA'] == pivot]
        right = [x for x in arr if x['CGPA'] < pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]['CGPA'] > right[j]['CGPA']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def print_top_10(students):
    print("\nTop 10 Students by CGPA:")
    print("{:<5} {:<20} {:<15} {:<5}".format("Rank", "Name", "Roll No", "CGPA"))
    for idx, student in enumerate(students[:10], 1):
        print("{:<5} {:<20} {:<15} {:.2f}".format(idx, student['Name'], student['Roll'], student['CGPA']))

def generate_large_dataset(size):
    students = []
    for i in range(size):
        name = f"Student_{i+1}"
        roll = f"R{1000+i}"
        cgpa = round(random.uniform(5.0, 10.0), 2)
        students.append({'Name': name, 'Roll': roll, 'CGPA': cgpa})
    return students

def compare_algorithms():
    size = int(input("\nEnter size of large dataset for performance comparison: "))
    dataset = generate_large_dataset(size)
    dataset_qs = list(dataset)
    dataset_ms = list(dataset)

    start = time.time()
    sorted_qs = quick_sort(dataset_qs)
    end = time.time()
    print(f"Quick Sort Time: {end - start:.6f} seconds")

    start = time.time()
    sorted_ms = merge_sort(dataset_ms)
    end = time.time()
    print(f"Merge Sort Time: {end - start:.6f} seconds")

    print("\nTop 10 students from Quick Sort result:")
    print_top_10(sorted_qs)
    print("\nTop 10 students from Merge Sort result:")
    print_top_10(sorted_ms)

def main():
    print("SR University Placement Drive - Student Record Sorting\n")
    students = get_student_records()
    print("\nChoose sorting algorithm:")
    print("1. Quick Sort")
    print("2. Merge Sort")
    choice = input("Enter choice (1/2): ")
    if choice == '1':
        sorted_students = quick_sort(students)
    else:
        sorted_students = merge_sort(students)
    print_top_10(sorted_students)

    # Performance comparison on large dataset
    compare = input("\nDo you want to compare performance on a large dataset? (y/n): ")
    if compare.lower() == 'y':
        compare_algorithms()

if __name__ == "__main__":
    main()
