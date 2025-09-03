from Task_5 import convert_date_format


def run_tests_for_convert_date_format():
    test_cases = [
        ("2023-01-31", "31-01-2023"),
        ("0001-12-09", "09-12-0001"),
        # Accepts digit-only with exact lengths; does not validate calendar ranges
        ("2023-13-01", "01-13-2023"),
        # Invalid formats
        ("2023-1-01", "Invalid date format. Please use YYYY-MM-DD."),
        ("23-01-01", "Invalid date format. Please use YYYY-MM-DD."),
        ("2023-01-1", "Invalid date format. Please use YYYY-MM-DD."),
        ("2023/01/01", "Invalid date format. Please use YYYY-MM-DD."),
        ("abcd-ef-gh", "Invalid date format. Please use YYYY-MM-DD."),
        ("2023-01", "Invalid date format. Please use YYYY-MM-DD."),
        ("", "Invalid date format. Please use YYYY-MM-DD."),
        (" 2023-01-01 ", "Invalid date format. Please use YYYY-MM-DD."),
    ]

    passed = 0
    for idx, (inp, expected) in enumerate(test_cases, 1):
        result = convert_date_format(inp)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test case {idx}: convert_date_format({repr(inp)}) -> Expected: {repr(expected)}, Got: {repr(result)} [{status}]"
        )
        if status == "PASS":
            passed += 1
    print(f"\n{passed}/{len(test_cases)} test cases passed.")


if __name__ == "__main__":
    print("Running test cases for convert_date_format(date_str):\n")
    run_tests_for_convert_date_format()


