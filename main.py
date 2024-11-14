
def display_menu():
    print("Store Menu\n----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")
    choice = input("Please choose a number: ")
    return choice

products = [
    {"name": "Laptop", "quantity": 10, "price": 1200},
    {"name": "Smartphone", "quantity": 15, "price": 800},
    {"name": "Tablet", "quantity": 20, "price": 300},
]

def list_products():
    print("\nAvailable Products:")
    for product in products:
        print(f"{product['name']} - ${product['price']} ({product['quantity']} available)")
print()


def show_total_amount():
    total = sum(product['quantity'] for product in products)
    print(f"\nTotal products in store: {total}\n")


def make_order():
    order_product = input("Enter the product name you want to order: ")
    order_quantity = int(input("Enter the quantity: "))
    for product in products:
        if product["name"].lower() == order_product.lower():
            if product["quantity"] >= order_quantity:
                product["quantity"] -= order_quantity
                print(f"Order successful! {order_quantity} {product['name']} ordered.\n")
            else:
                print(f"Sorry, only {product['quantity']} available.\n")
            return

    print("Product not found in store.\n")


def main():
    while True:
        choice = display_menu()
        if choice == "1":
            list_products()
        elif choice == "2":
            show_total_amount()
        elif choice == "3":
            make_order()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
