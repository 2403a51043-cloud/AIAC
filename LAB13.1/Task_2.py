def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage example
file_path = r"C:\Users\manic\OneDrive\Desktop\poem.txt"
result = read_file(file_path)
if result is not None:
    print("File contents:")
    print(result)