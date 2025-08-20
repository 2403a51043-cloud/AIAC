import hashlib

def hash_email(email):
    # Hash the email using SHA-256 for anonymization
    return hashlib.sha256(email.encode()).hexdigest()

def main():
    # Collect user data
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    # Anonymize email by hashing
    hashed_email = hash_email(email)

    # Do NOT store or print the original email
    # Store only anonymized (hashed) email and minimal necessary data
    user_data = {
        "name": name,  # Consider pseudonymizing or encrypting names for more privacy
        "age": age,    # Consider storing age ranges instead of exact age
        "mail": hashed_email
    }

    print("Collected (protected) user data:")
    print(user_data)

    # Comments on data protection:
    # - Never store sensitive data (like emails) in plain text.
    # - Use strong hashing algorithms (e.g., SHA-256) for anonymization.
    # - For higher security, consider encrypting all personal data.
    # - Limit access to the data and follow data protection regulations.

if __name__ == "__main__":
    main()