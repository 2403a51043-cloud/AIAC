# INSERT_YOUR_CODE
def convert_date_format(date_str):
    # Expects date_str in "YYYY-MM-DD"
    try:
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError
        yyyy, mm, dd = parts
        if len(yyyy) != 4 or len(mm) != 2 or len(dd) != 2:
            raise ValueError
        # Optionally, check if all are digits
        if not (yyyy.isdigit() and mm.isdigit() and dd.isdigit()):
            raise ValueError
        return f"{dd}-{mm}-{yyyy}"
    except Exception:
        return "Invalid date format. Please use YYYY-MM-DD."

def main():
    user_input = input("Enter a date (YYYY-MM-DD): ").strip()
    result = convert_date_format(user_input)
    print(result)

if __name__ == "__main__":
    main()

