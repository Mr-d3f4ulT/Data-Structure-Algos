# SHOPPING CART PROGRAM


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a whole number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


def display_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n--- YOUR SHOPPING CART ---")
    print(f"{'No.':<4}{'Item':<20}{'Qty':<6}{'Price':<10}{'Subtotal'}")
    print("-" * 55)

    for index, item in enumerate(cart, start=1):
        subtotal = item["price"] * item["quantity"]
        print(
            f"{index:<4}{item['name']:<20}{item['quantity']:<6}"
            f"${item['price']:<9.2f}${subtotal:.2f}"
        )

    print("-" * 55)
    print(f"Total: ${calculate_total(cart):.2f}")


def calculate_total(cart):
    return sum(item["price"] * item["quantity"] for item in cart)


def add_item(cart):
    name = input("\nEnter item name: ").strip()
    if not name:
        print("Item name cannot be empty.")
        return

    price = get_positive_float(f"Enter the price of {name}: $")
    quantity = get_positive_int(f"Enter the quantity of {name}: ")

    cart.append({"name": name, "price": price, "quantity": quantity})
    print(f"{quantity} x {name} added to your cart.")


def remove_item(cart):
    if not cart:
        print("\nYour cart is empty. Nothing to remove.")
        return

    display_cart(cart)
    item_number = get_positive_int("\nEnter the item number to remove: ")

    if item_number > len(cart):
        print("That item number does not exist.")
        return

    removed_item = cart.pop(item_number - 1)
    print(f"Removed {removed_item['name']} from your cart.")


def checkout(cart):
    display_cart(cart)
    print("\nThank you for shopping with us!")


def main():
    cart = []

    while True:
        print("\n--- SHOPPING CART MENU ---")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Checkout")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            display_cart(cart)
        elif choice == "3":
            remove_item(cart)
        elif choice == "4":
            checkout(cart)
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
