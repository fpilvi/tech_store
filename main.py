from products import Product
from store import Store

# start stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]

# start the store with the product list
best_buy = Store(product_list)


def list_products(store: Store):
    """all active products in store."""
    print("\nList of all products in the store:")
    for product in store.get_all_products():
        print(product.show())


def show_total_amount(store: Store):
    """total amount of products in store."""
    total_quantity = store.get_total_quantity()
    print(f"\nTotal quantity of all products in the store: {total_quantity}")


def make_order(store: Store):
    """user to make an order."""
    shopping_list = []

    print("\nEnter your order:")
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break

        # find product in store
        product = None
        for p in store.get_all_products():
            if p.name.lower() == product_name.lower():
                product = p
                break

        if product:
            try:
                quantity = int(input(f"How many {product_name}s would you like to buy? "))
                shopping_list.append((product, quantity))
            except ValueError:
                print("Please enter a valid number for quantity.")
        else:
            print(f"Sorry, we don't have {product_name} in the store.")

    if shopping_list:
        total_price = store.order(shopping_list)
        print(f"\nYour total order price is: ${total_price:.2f}")
    else:
        print("No products added to the order.")


def start(store: Store):
    """start user internface."""
    while True:
        print("\nStore Menu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_amount(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Thank you for visiting the store!")
            break
        else:
            print("Invalid choice, please try again.")



start(best_buy)
