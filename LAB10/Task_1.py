def discount(price, category):
        if category == "student":
            return price * 0.9 if price > 1000 else price * 0.95
        if price > 2000:
            return price * 0.85
        return price
if __name__ == "__main__":
        price = float(input("Enter the price: "))
        category = input("Enter the category: ")
        final_price = discount(price, category)
        print(f"Discounted price: {final_price}")


