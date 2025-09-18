import unittest
from bisect import insort, bisect_left

def rolling_median(nums, w):
    n = len(nums)
    if w > n or w <= 0:
        return []
    window = sorted(nums[:w])
    medians = []
    for i in range(w, n + 1):
        if w % 2 == 1:
            medians.append(window[w // 2])
        else:
            medians.append((window[w // 2 - 1] + window[w // 2]) / 2)
        if i == n:
            break
        out_elem = nums[i - w]
        idx = bisect_left(window, out_elem)
        window.pop(idx)
        insort(window, nums[i])
    return medians

class TestRollingMedian(unittest.TestCase):

    def test_TC01(self):
        self.assertEqual(rolling_median([1, 3, 2, 7, 5], 3), [2, 3, 5])

    def test_TC02(self):
        self.assertEqual(rolling_median([1, 2, 3, 4], 2), [1.5, 2.5, 3.5])

    def test_TC03(self):
        self.assertEqual(rolling_median([5, 10, 15], 1), [5, 10, 15])

    def test_TC04(self):
        self.assertEqual(rolling_median([8, 6, 4, 2], 4), [5.0])

    def test_TC05(self):
        self.assertEqual(rolling_median([], 3), [])

    def test_TC06(self):
        self.assertEqual(rolling_median([1, 2, 3], 0), [])

    def test_TC07(self):
        self.assertEqual(rolling_median([1, 2, 3], 4), [])

    def test_TC08(self):
        self.assertEqual(rolling_median([7, 7, 7, 7], 2), [7.0, 7.0, 7.0])

    def test_TC09(self):
        self.assertEqual(rolling_median([1, 5, 2, 4, 3], 5), [3])

    def test_TC10(self):
        self.assertEqual(rolling_median([10, 20, 30, 40, 50], 2), [15.0, 25.0, 35.0, 45.0])

    def test_TC11(self):
        self.assertEqual(rolling_median([50, 40, 30, 20, 10], 2), [45.0, 35.0, 25.0, 15.0])

    def test_TC12(self):
        self.assertEqual(rolling_median([1, 3, 5, 7, 9], 3), [3, 5, 7])

    def test_TC13(self):
        self.assertEqual(rolling_median([9, 7, 5, 3, 1], 3), [7, 5, 3])

    def test_TC14(self):
        self.assertEqual(rolling_median([1, 2, 3, 4, 5, 6], 6), [3.5])

if __name__ == "__main__":
    unittest.main()
print("All the test cases are passed")