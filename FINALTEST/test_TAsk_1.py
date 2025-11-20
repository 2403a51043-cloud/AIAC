import unittest
from TAsk_1 import get_highest_rated_product

class TestGetHighestRatedProduct(unittest.TestCase):
    """Test cases for get_highest_rated_product function."""
    
    def test_single_product(self):
        """Test with a single product."""
        products = [("Laptop", 4.5)]
        self.assertEqual(get_highest_rated_product(products), ("Laptop", 4.5))
    
    def test_multiple_products(self):
        """Test with multiple products."""
        products = [("Laptop", 4.5), ("Mouse", 4.8), ("Keyboard", 4.2)]
        self.assertEqual(get_highest_rated_product(products), ("Mouse", 4.8))
    
    def test_highest_at_beginning(self):
        """Test when highest-rated product is first."""
        products = [("Product1", 5.0), ("Product2", 3.5), ("Product3", 2.0)]
        self.assertEqual(get_highest_rated_product(products), ("Product1", 5.0))
    
    def test_highest_at_end(self):
        """Test when highest-rated product is last."""
        products = [("Product1", 2.0), ("Product2", 3.5), ("Product3", 5.0)]
        self.assertEqual(get_highest_rated_product(products), ("Product3", 5.0))
    
    def test_equal_ratings(self):
        """Test with equal ratings (returns first occurrence)."""
        products = [("ProductA", 4.5), ("ProductB", 4.5)]
        self.assertEqual(get_highest_rated_product(products), ("ProductA", 4.5))
    
    def test_empty_list_raises_error(self):
        """Test that ValueError is raised for empty list."""
        with self.assertRaises(ValueError) as context:
            get_highest_rated_product([])
        self.assertIn("Product list cannot be empty.", str(context.exception))
    
    def test_negative_ratings(self):
        """Test with negative ratings."""
        products = [("Product1", -1.5), ("Product2", -0.5), ("Product3", -2.0)]
        self.assertEqual(get_highest_rated_product(products), ("Product2", -0.5))
    
    def test_zero_rating(self):
        """Test with zero ratings."""
        products = [("Product1", 0.0), ("Product2", 1.5)]
        self.assertEqual(get_highest_rated_product(products), ("Product2", 1.5))

if __name__ == '__main__':
    unittest.main()