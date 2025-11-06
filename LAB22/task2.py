from PIL import Image

def compress_and_resize(input_path, output_path, quality, width, height):
    """
    Compress and resize an image to smaller dimensions.
    """
    try:
        # Open image
        image = Image.open(input_path)

        # Resize image
        image = image.resize((width, height))

        # Compress and save
        image.save(output_path, "JPEG", optimize=True, quality=quality)

        print(f"✅ Image resized to {width}x{height} and compressed (quality={quality}).")
        print(f"Saved as '{output_path}'")

    except FileNotFoundError:
        print("❌ Error: Image file not found.")
    except Exception as e:
        print("⚠️ Error:", e)


# -----------------------------
# Main Program
# -----------------------------
print("🖼️ Image Compression and Resizing Tool\n")

input_file = input("Enter the image filename (e.g., sample.jpg): ").strip()
output_file = input("Enter output filename (e.g., small.jpg): ").strip()
quality = int(input("Enter image quality (1-100, lower = smaller file): "))
width = int(input("Enter new width in pixels (e.g., 100): "))
height = int(input("Enter new height in pixels (e.g., 100): "))

compress_and_resize(input_file, output_file, quality, width, height)
