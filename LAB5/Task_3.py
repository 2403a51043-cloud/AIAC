import random

# Product Recommendation System
# Recommends products based on user's purchase history, ensures fairness, and learns from feedback.


# Sample product catalog with brands and categories
products = [
    {"name": "EcoClean Detergent", "brand": "EcoBrand", "category": "Cleaning"},
    {"name": "Sparkle Detergent", "brand": "SparkleCo", "category": "Cleaning"},
    {"name": "FreshBite Apples", "brand": "FarmFresh", "category": "Fruits"},
    {"name": "JuicyRed Apples", "brand": "RedOrchard", "category": "Fruits"},
    {"name": "QuickCharge Powerbank", "brand": "Techie", "category": "Electronics"},
    {"name": "PowerPlus Powerbank", "brand": "GadgetPro", "category": "Electronics"},
]

# User purchase history and feedback memory
purchase_history = []
feedback_memory = {}

def recommend_product():
    # Find categories the user bought before
    categories_bought = {p['category'] for p in purchase_history}
    # Recommend from those categories, but not same brand as last purchase
    recommendations = []
    for category in categories_bought:
        brands_bought = {p['brand'] for p in purchase_history if p['category'] == category}
        # Filter products in the same category, but different brand
        candidates = [p for p in products if p['category'] == category and p['brand'] not in brands_bought]
        # If all brands bought, recommend any in category
        if not candidates:
            candidates = [p for p in products if p['category'] == category]
        # Shuffle to ensure fairness
        random.shuffle(candidates)
        for c in candidates:
            # Avoid recommending disliked products
            if feedback_memory.get(c['name'], 0) >= 0:
                recommendations.append(c)
                break
    return recommendations

def explain_recommendation(product):
    # Explain based on category and brand diversity
    explanation = f"We recommend '{product['name']}' from {product['brand']} because you bought items in the '{product['category']}' category before, and this is a different brand for variety."
    return explanation

def get_feedback(product):
    # Ask user for feedback
    feedback = input(f"Do you like the recommendation '{product['name']}'? (like/dislike): ").strip().lower()
    if feedback == "like":
        feedback_memory[product['name']] = feedback_memory.get(product['name'], 0) + 1
        print("Thanks for your feedback! We'll suggest more like this.")
    elif feedback == "dislike":
        feedback_memory[product['name']] = feedback_memory.get(product['name'], 0) - 1
        print("Thanks for your feedback! We'll avoid similar products.")
    else:
        print("Feedback not recognized. Skipping.")

def main():
    print("Welcome to the Product Recommendation System!")
    # Simulate user purchases
    while True:
        print("\nYour purchase history:")
        if purchase_history:
            for p in purchase_history:
                print(f"- {p['name']} ({p['brand']}, {p['category']})")
        else:
            print("No purchases yet.")
        # Let user add a purchase
        print("\nAvailable products:")
        for idx, p in enumerate(products):
            print(f"{idx+1}. {p['name']} ({p['brand']}, {p['category']})")
        choice = input("Enter the number of a product you bought (or 'q' to quit): ").strip()
        if choice.lower() == 'q':
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(products):
                purchase_history.append(products[idx])
            else:
                print("Invalid choice.")
                continue
        except ValueError:
            print("Invalid input.")
            continue

        # Recommend products
        recs = recommend_product()
        if recs:
            print("\nRecommended products for you:")
            for rec in recs:
                print(f"- {rec['name']} ({rec['brand']}, {rec['category']})")
                print("  " + explain_recommendation(rec))
                get_feedback(rec)
        else:
            print("No recommendations available yet.")

if __name__ == "__main__":
    main()