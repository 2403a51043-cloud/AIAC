def area_rectangle(length, width):
    return length * width

def area_square(side):
    return side * side

def area_circle(radius):
    return 3.14 * radius * radius

def calculate_area(shape, x, y=0):
    dispatch = {
        "rectangle": lambda: area_rectangle(x, y),
        "square": lambda: area_square(x),
        "circle": lambda: area_circle(x)
    }
    if shape not in dispatch:
        raise ValueError(f"Unknown shape: {shape}")
    return dispatch[shape]()

if __name__ == "__main__":
    shape = input("Enter shape (rectangle, square, circle): ").strip().lower()
    if shape == "rectangle":
        x = float(input("Enter length: "))
        y = float(input("Enter width: "))
        area = calculate_area(shape, x, y)
    elif shape == "square":
        x = float(input("Enter side: "))
        area = calculate_area(shape, x)
    elif shape == "circle":
        x = float(input("Enter radius: "))
        area = calculate_area(shape, x)
    else:
        print("Unknown shape.")
        exit(1)
    print(f"Area of {shape}: {area}")