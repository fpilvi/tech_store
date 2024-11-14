from products import Product

class Store:
    def __init__(self):
        """building the store and a new empty warehouse."""
        self.products = []

    def add_product(self, product):
        """puts new products to the store."""
        self.products.append(product)

    def list_products(self):
        """lists all products."""
        if not self.products:
            print("No products available.")
            return
        for product in self.products:
            print(product.show())

    def total_inventory_value(self):
        """value of inventory."""
        total = 0
        for product in self.products:
            total += product.get_quantity() * product.price
        print(f"Total value of inventory: {total}")

    def make_order(self):
        """user can buy a product and gives back the total price."""
        self.list_products()
        product_name = input("Enter the product you want to buy: ")
        quantity = int(input("Enter the quantity: "))
        product = next((p for p in self.products if p.name == product_name), None)

        if product:
            try:
                total_price = product.buy(quantity)
                print(f"Total price for {quantity} {product_name}: {total_price}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Product not found.")

#test
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    store = Store()
    store.add_product(bose)
    store.add_product(mac)
    store.list_products()
    store.total_inventory_value()
    store.make_order()