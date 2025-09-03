# INSERT_YOUR_CODE
def is_valid_mail(mail):
    # Check for exactly one '@'
    if mail.count('@') != 1:
        return False
    local, domain = mail.split('@')
    # Both local and domain must be non-empty and contain only allowed characters (letters, digits, . and _ and -)
    if not local or not domain:
        return False
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-")
    for part in (local, domain):
        if not all(c in allowed for c in part):
            return False
    return True

def check_mail():
    mail = input("Enter your mail: ")
    if is_valid_mail(mail):
        print("Valid mail address.")
    else:
        print("Invalid mail address.")

# Example usage:
# check_mail()
# INSERT_YOUR_CODE
mail = input("Enter your mail: ")
if is_valid_mail(mail):
    print("Valid mail address.")
else:
    print("Invalid mail address.")
