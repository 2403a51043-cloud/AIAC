from Task_4 import ShoppingCart


def run_tests_for_shopping_cart():
    passed = 0
    total = 0

    def check(name, condition, details=""):
        nonlocal passed, total
        total += 1
        status = "PASS" if condition else "FAIL"
        print(f"{name}: [{status}]" + (f" - {details}" if details else ""))
        if condition:
            passed += 1

    # Test 1: Add single item
    cart = ShoppingCart()
    cart.add_item("apple", 1.50, 2)
    check(
        "Add item stores correct price and quantity",
        cart.items.get("apple") == (1.50, 2),
        details=str(cart.items.get("apple")),
    )

    # Test 2: Add same item again increases quantity and may update price
    cart.add_item("apple", 1.50, 3)
    check(
        "Add same item accumulates quantity",
        cart.items.get("apple") == (1.50, 5),
        details=str(cart.items.get("apple")),
    )

    # Test 3: Add new item
    cart.add_item("banana", 0.80, 4)
    check(
        "Add new item tracked",
        cart.items.get("banana") == (0.80, 4),
        details=str(cart.items.get("banana")),
    )

    # Test 4: Total cost calculation
    expected_total = 1.50 * 5 + 0.80 * 4
    check(
        "Total cost is correct",
        abs(cart.total_cost() - expected_total) < 1e-9,
        details=f"got={cart.total_cost()}, expected={expected_total}",
    )

    # Test 5: Remove partial quantity
    cart.remove_item("banana", 2)
    check(
        "Remove partial quantity updates item",
        cart.items.get("banana") == (0.80, 2),
        details=str(cart.items.get("banana")),
    )

    # Test 6: Remove all of an item
    cart.remove_item("banana", 5)  # more than remaining should delete
    check(
        "Remove all deletes item entry",
        "banana" not in cart.items,
    )

    # Test 7: Removing non-existent item should not error
    try:
        cart.remove_item("cherry", 1)
        no_error = True
    except Exception:
        no_error = False
    check("Remove non-existent item does not raise", no_error)

    # Test 8: Price change on re-add updates stored price and quantity
    cart.add_item("orange", 1.00, 1)
    cart.add_item("orange", 1.20, 2)  # price update warning expected, but we test state
    check(
        "Re-adding with new price updates price and accumulates quantity",
        cart.items.get("orange") == (1.20, 3),
        details=str(cart.items.get("orange")),
    )

    # Test 9: Total after series of operations
    # Current items: apple (1.50 x 5), orange (1.20 x 3)
    expected_total = 1.50 * 5 + 1.20 * 3
    check(
        "Final total cost is correct",
        abs(cart.total_cost() - expected_total) < 1e-9,
        details=f"got={cart.total_cost()}, expected={expected_total}",
    )

    print(f"\n{passed}/{total} test cases passed.")


if __name__ == "__main__":
    print("Running test cases for ShoppingCart:\n")
    run_tests_for_shopping_cart()


