from Task_2 import assign_grade


def run_tests_for_assign_grade():
    test_cases = [
        (100, "A"),
        (90, "A"),
        (89, "B"),
        (80, "B"),
        (79, "C"),
        (70, "C"),
        (69, "D"),
        (60, "D"),
        (59, "F"),
        (0, "F"),
        (89.0, "B"),
        (79.0, "C"),
        (69.0, "D"),
        (59.0, "F"),
        (-1, "Invalid input: Score must be between 0 and 100."),
        (101, "Invalid input: Score must be between 0 and 100."),
        ("eighty", "Invalid input: Score must be a number."),
        (None, "Invalid input: Score must be a number."),
        ([90], "Invalid input: Score must be a number."),
        ({'score': 90}, "Invalid input: Score must be a number."),
    ]

    passed = 0
    for idx, (inp, expected) in enumerate(test_cases, 1):
        result = assign_grade(inp)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test case {idx}: assign_grade({repr(inp)}) -> Expected: {repr(expected)}, Got: {repr(result)} [{status}]"
        )
        if status == "PASS":
            passed += 1
    print(f"\n{passed}/{len(test_cases)} test cases passed.")


if __name__ == "__main__":
    print("Running test cases for assign_grade(score):\n")
    run_tests_for_assign_grade()