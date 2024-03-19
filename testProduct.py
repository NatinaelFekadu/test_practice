import unittest
from product import Product  

class TestProduct(unittest.TestCase):
    def test_init(self):
        
        product = Product("Test Product", 10, 5)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 10)
        self.assertEqual(product.quantity, 5)

    def test_calculateTotal(self):
        
        product = Product("Test Product", 10, 5)
        self.assertEqual(product.calculateTotal(), 50)

    def test_with_zero_values(self):    
        product = Product("Test Product", 10, 0)
        self.assertEqual(product.calculateTotal(), 0)
        
        product = Product("Test Product", 0, 5)
        self.assertEqual(product.calculateTotal(), 0)
        
        product = Product("Test Product", 0, 0)
        self.assertEqual(product.calculateTotal(), 0)
        
    def test_calculateTotal_with_negative_values(self):
        product = Product("Test Product", -10, 5)
        with self.assertRaises(ValueError):
            product.calculateTotal()

        product = Product("Test Product", 10, -5)
        with self.assertRaises(ValueError):
            product.calculateTotal()

        product = Product("Test Product", -10, -5)
        with self.assertRaises(ValueError):
            product.calculateTotal()

if __name__ == '__main__':
    unittest.main()
