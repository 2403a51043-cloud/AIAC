"""
Program: Highest-Rated Product Finder
-------------------------------------
This program allows the user to enter product names and ratings.
It then finds and displays the highest-rated product.
"""

def get_highest_rated_product(product_list):
    """
    Find and return the product with the highest rating from a list of products.
    Args:
        product_list (list): A list of tuples where each tuple contains 
                           (product_name, rating, ...).
    Returns:
        tuple: The product tuple with the highest rating value.
    Raises:
        ValueError: If the product_list is empty.
    Example:
        >>> products = [("Laptop", 4.5), ("Mouse", 4.8), ("Keyboard", 4.2)]
        >>> get_highest_rated_product(products)
        ('Mouse', 4.8)
    """
    # Ensure the list is not empty
    if not product_list:
        raise ValueError("Product list cannot be empty.")
    
    # Use max with a key function to find highest rating
    return max(product_list, key=lambda x: x[1])


if __name__ == "__main__":
    # Ask user how many products they want to enter
    n = int(input("How many products do you want to enter? "))
    
    products = []

    # Take product details from the user
    for i in range(n):
        name = input(f"Enter product {i+1} name: ")
        rating = float(input(f"Enter rating for {name}: "))
        products.append((name, rating))

    # Find and display the highest-rated product
    highest = get_highest_rated_product(products)
    print("\nHighest Rated Product:", highest)


# ----------- Simple Tests -----------
def test():
    # Test with predefined product rating list
    sample = [("A", 3.1), ("B", 4.7), ("C", 4.4)]
    print("Test Result:", get_highest_rated_product(sample))

# Run test function
test()
