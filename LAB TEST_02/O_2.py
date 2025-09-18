from bisect import insort, bisect_left

def rolling_median(nums, w):
    """
    Returns the median for each sliding window of size w in nums.
    Uses a sorted window with bisect for efficient insertion/removal.
    Acceptance Criteria: Efficient and correct. Edges: short lists, window equals list length, empty list.
    """
    n = len(nums)
    if w > n or w <= 0:
        return []
    window = sorted(nums[:w])
    medians = []
    for i in range(w, n + 1):
        # Compute median
        if w % 2 == 1:
            medians.append(window[w // 2])
        else:
            medians.append((window[w // 2 - 1] + window[w // 2]) / 2)
        if i == n:
            break
        # Remove outgoing element
        out_elem = nums[i - w]
        idx = bisect_left(window, out_elem)
        window.pop(idx)
        # Insert incoming element
        insort(window, nums[i])
    return medians

if __name__ == "__main__":
    print("Enter the list of numbers separated by spaces:")
    try:
        nums = list(map(int, input().strip().split()))
    except Exception:
        print("Invalid input. Please enter integers separated by spaces.")
        exit(1)
    print("Enter the window size (integer):")
    try:
        w = int(input())
    except Exception:
        print("Invalid window size. Please enter an integer.")
        exit(1)
    result = rolling_median(nums, w)
    print("Expected output:")
    print(result)
    print("Acceptance Criteria: Efficient and correct. Handles short lists, window equals list length, and empty list.")


