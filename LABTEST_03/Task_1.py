def merge_sort(arr):
    # If array has one element, no sorting needed
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Divide the array into two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    merged = merge(left, right)

    print(f"Merging {left} and {right} --> {merged}")
    return merged


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -------- MAIN PROGRAM --------
# User input
user_input = input("Enter integers separated by space: ")

# Convert string input to list of integers
num_list = list(map(int, user_input.split()))

print("\n--- Merge Sort Steps ---")
sorted_list = merge_sort(num_list)

print("\nFinal Sorted List:", sorted_list)
