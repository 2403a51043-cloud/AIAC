file_path = r"C:\Users\manic\OneDrive\Desktop\poem.txt"
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")
except FileNotFoundError:
    print("File not found.")
