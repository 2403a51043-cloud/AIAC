# INSERT_YOUR_CODE

def run_test_cases():
    test_cases = [
        # (input, expected_output)
        ("user@example.com", True),
        ("user.name-123@domain.co", True),
        ("user@sub.domain.com", True),
        ("user@domain", True),
        ("user@domain.c", True),
        ("user@domain..com", True),  # double dot in domain is allowed by current logic
        ("user@domain_com", True),   # underscore in domain is allowed by current logic
        ("user@domain-com", True),
        ("user@domain.com-", True),
        ("user@domain.com_", True),
        ("user@domain.com.", True),
        ("user@domaincom", True),
        ("user@domain@com", False),  # more than one '@'
        ("userdomain.com", False),   # no '@'
        ("@domain.com", False),      # empty local part
        ("user@", False),            # empty domain part
        ("user!@domain.com", False), # invalid char '!' in local
        ("user@domain!.com", False), # invalid char '!' in domain
        ("user name@domain.com", False), # space in local
        ("user@domain com", False),      # space in domain
        ("", False),                     # empty string
        ("user@.com", True),             # domain starts with dot, allowed by current logic
        (".user@domain.com", True),      # local starts with dot, allowed by current logic
        ("user@domain..com", True),      # double dot in domain, allowed by current logic
    ]

    from Task_1 import is_valid_mail

    passed = 0
    for idx, (mail, expected) in enumerate(test_cases, 1):
        result = is_valid_mail(mail)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test case {idx}: '{mail}' -> Expected: {expected}, Got: {result} [{status}]")
        if status == "PASS":
            passed += 1
    print(f"\n{passed}/{len(test_cases)} test cases passed.")

if __name__ == "__main__":
    run_test_cases()

