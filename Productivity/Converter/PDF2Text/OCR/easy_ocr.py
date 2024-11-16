import easyocr
import torch

# Function to check if GPU is available
def check_gpu():
    if torch.cuda.is_available():
        print("GPU is available and will be used.")
    else:
        print("GPU is not available. Using CPU.")

# Check GPU availability
check_gpu()

# Initialize EasyOCR reader for Traditional Chinese (zh-tw)
reader = easyocr.Reader(['ch_tra', 'en'], gpu=True)  # Set gpu=True to ensure it uses GPU

# Loop through image files from 001 to 274
for i in range(1, 275):  # Loop from 1 to 274
    # Format the image file name
    image_file = f'output-{i:03}.png'  # This formats numbers with leading zeros (e.g., 001, 002, ..., 274)
    
    try:
        # Perform OCR on the image
        result = reader.readtext(image_file)

        # Create corresponding .txt file name
        output_file = image_file.replace('.png', '.txt')  # Replace .png with .txt

        # Save the recognized text to a .txt file
        with open(output_file, 'w', encoding='utf-8') as f:
            for detection in result:
                text = detection[1]  # The recognized text
                f.write(text + '\n')  # Write text to file, each on a new line

        print(f'Text from {image_file} saved to {output_file}')
    
    except Exception as e:
        print(f"Error processing {image_file}: {e}")