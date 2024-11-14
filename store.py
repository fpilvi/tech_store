from typing import List
import products


class Store:
    def __init__(self, products: List[products.Product]):
        self.products = products

    def add_product(self, product: products.Product):
        """adds products to the store."""
        self.products.append(product)

    def remove_product(self, product: products.Product):
        """delets products from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """gives back the total price of all products in store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[products.Product]:
        """Gives back all products in store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """sets an order and gives back the total price."""
        total_price = 0.0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except Exception as e:
                print(f"Error purchasing {product.show()}: {e}")
        return total_price
