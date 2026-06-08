# Concession stand program

menu = {
    "hot dog": 3.50,
    "popcorn": 4.00,
    "soda": 2.50,
    "candy": 1.75,
    "nachos": 5.00,
    "pretzel": 4.50,
    "ice cream": 6.00,
    "chips": 2.25,
}


def get_positive_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Please enter a whole number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def display_menu():
    print("\n----------------- MENU -----------------")
    for number, (food, price) in enumerate(menu.items(), start=1):
        print(f"{number}. {food.title():40} ${price:.2f}")
    print("----------------------------------------")


def calculate_total(cart):
    return sum(menu[food] * quantity for food, quantity in cart.items())


def display_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n------------- YOUR ORDER -------------")
    print(f"{'Item':<14}{'Qty':<6}{'Price':<10}{'Subtotal'}")
    print("-" * 40)

    for food, quantity in cart.items():
        price = menu[food]
        subtotal = price * quantity
        print(f"{food.title():<14}{quantity:<6}${price:<9.2f}${subtotal:.2f}")

    print("-" * 40)
    print(f"Total: ${calculate_total(cart):.2f}")


def choose_menu_item():
    menu_items = list(menu.keys())

    while True:
        choice = input("Enter item name, item number, or 'q' to cancel: ").strip().lower()

        if choice == "q":
            return None

        if choice.isdigit():
            item_number = int(choice)
            if 1 <= item_number <= len(menu_items):
                return menu_items[item_number - 1]

        if choice in menu:
            return choice

        print("Sorry, that item is not on the menu.")


def add_item(cart):
    display_menu()
    food = choose_menu_item()

    if food is None:
        print("No item added.")
        return

    quantity = get_positive_int(f"How many {food}s would you like? ")
    cart[food] = cart.get(food, 0) + quantity
    print(f"Added {quantity} {food}(s) to your cart.")


def remove_item(cart):
    if not cart:
        print("\nYour cart is empty. Nothing to remove.")
        return

    display_cart(cart)
    food = input("\nEnter the item name to remove: ").strip().lower()

    if food not in cart:
        print("That item is not in your cart.")
        return

    del cart[food]
    print(f"Removed {food} from your cart.")


def checkout(cart):
    display_cart(cart)
    print("\nEnjoy your snacks!")


def main():
    cart = {}

    while True:
        print("\n---------- CONCESSION STAND ----------")
        print("1. Show menu")
        print("2. Add item")
        print("3. View cart")
        print("4. Remove item")
        print("5. Checkout")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_menu()
        elif choice == "2":
            add_item(cart)
        elif choice == "3":
            display_cart(cart)
        elif choice == "4":
            remove_item(cart)
        elif choice == "5":
            checkout(cart)
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
