import os
from PIL import Image

def ICO2PNG(input_path):
    # Extract filename without extension from the input path
    base_name = os.path.basename(input_path)  # gets filename with extension
    filename_without_extension = os.path.splitext(base_name)[0]
    save_path = os.path.join(filename_without_extension + '.png')

    # Convert ICO to PNG using Pillow
    img = Image.open(input_path)
    img.save(save_path)
    img.close()  # Close the image to release the file lock

    print(f"Icon converted and saved to {save_path}")

# Example usage
if __name__ == "__main__":
    ICO2PNG("Control_Panel.ico")