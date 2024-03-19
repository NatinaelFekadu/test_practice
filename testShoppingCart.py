import unittest
from shoppingcart import ShoppingCart
from product import Product  

class TestShoppingCartIntegration(unittest.TestCase):
    def test_cart_total(self):
        
        cart = ShoppingCart()
        
        product1 = Product("Product 1", 10, 2)
        product2 = Product("Product 2", 20, 1)

        cart.addProduct(product1)  
        cart.addProduct(product2)  
        
        expected_total = (10 * 2) + (20 * 1)  
        actual_total = cart.calculateCartTotal()
        self.assertEqual(actual_total, expected_total)
        
    def test_with_zero_products(self):
        cart = ShoppingCart()
        self.assertEqual(cart.calculateCartTotal(), 0)
if __name__ == '__main__':
    unittest.main()
