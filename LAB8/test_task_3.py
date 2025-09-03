from Task_3 import is_sentence_palindrome


def run_tests_for_is_sentence_palindrome():
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("No 'x' in Nixon", True),
        ("Was it a car or a cat I saw?", True),
        ("Never odd or even", True),
        ("Madam", True),
        ("", True),  # empty string -> cleaned empty string equals reverse
        (" \/-\t\n", True),  # only non-alphanumeric -> cleaned empty -> palindrome
        ("race a car", False),
        ("Hello, World!", False),
        ("12321", True),
        ("1231", False),
        ("Able was I ere I saw Elba", True),
    ]

    passed = 0
    for idx, (inp, expected) in enumerate(test_cases, 1):
        result = is_sentence_palindrome(inp)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test case {idx}: is_sentence_palindrome({repr(inp)}) -> Expected: {repr(expected)}, Got: {repr(result)} [{status}]"
        )
        if status == "PASS":
            passed += 1
    print(f"\n{passed}/{len(test_cases)} test cases passed.")


if __name__ == "__main__":
    print("Running test cases for is_sentence_palindrome(sentence):\n")
    run_tests_for_is_sentence_palindrome()

