class Product:
    """product class."""

    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input for product.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """is giving back the quanity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets quanity of products and deactivets it when 0."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """gives true when product is active."""
        return self.active

    def activate(self):
        """Actives the product."""
        self.active = True

    def deactivate(self):
        """deactives the product."""
        self.active = False

    def show(self):
        """shows details."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """buys quanity of products and gives back the total price."""
        if quantity > self.quantity:
            raise Exception("Not enough stock available.")
        total_price = quantity * self.price
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price
