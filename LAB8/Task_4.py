# INSERT_YOUR_CODE
class ShoppingCart:
    def __init__(self):
        self.items = {}  # item_name: (price, quantity)

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            current_price, current_quantity = self.items[item_name]
            if current_price != price:
                print(f"Warning: Price for '{item_name}' updated from {current_price} to {price}.")
            self.items[item_name] = (price, current_quantity + quantity)
        else:
            self.items[item_name] = (price, quantity)
        print(f"Added {quantity} x '{item_name}' at ${price:.2f} each to the cart.")

    def remove_item(self, item_name, quantity=1):
        if item_name not in self.items:
            print(f"Item '{item_name}' not found in the cart.")
            return
        price, current_quantity = self.items[item_name]
        if quantity >= current_quantity:
            del self.items[item_name]
            print(f"Removed all '{item_name}' from the cart.")
        else:
            self.items[item_name] = (price, current_quantity - quantity)
            print(f"Removed {quantity} x '{item_name}' from the cart.")

    def total_cost(self):
        return sum(price * quantity for price, quantity in self.items.values())

    def show_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("Current items in your cart:")
        for item, (price, quantity) in self.items.items():
            print(f" - {item}: {quantity} x ${price:.2f} = ${price*quantity:.2f}")
        print(f"Total cost: ${self.total_cost():.2f}")

def main():
    cart = ShoppingCart()
    while True:
        print("\nOptions: add, remove, show, total, quit")
        choice = input("What would you like to do? ").strip().lower()
        if choice == "add":
            item = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter quantity: "))
                if price < 0 or quantity <= 0:
                    print("Price must be non-negative and quantity must be positive.")
                    continue
            except ValueError:
                print("Invalid price or quantity.")
                continue
            cart.add_item(item, price, quantity)
        elif choice == "remove":
            item = input("Enter item name to remove: ").strip()
            try:
                quantity = int(input("Enter quantity to remove: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
            except ValueError:
                print("Invalid quantity.")
                continue
            cart.remove_item(item, quantity)
        elif choice == "show":
            cart.show_cart()
        elif choice == "total":
            total = cart.total_cost()
            print(f"Total cost of your cart: ${total:.2f}")
        elif choice == "quit":
            print("Thank you for shopping! Here is your final cart:")
            cart.show_cart()
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

