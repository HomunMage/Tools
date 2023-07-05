import os
import sys
from pdf2image import convert_from_path

def convert_pdf_to_image(pdf_path, output_dir):
    # Get the filename without extension
    filename = os.path.splitext(os.path.basename(pdf_path))[0]

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Save each image
    for i, image in enumerate(images):
        image.save(os.path.join(output_dir, f'{filename}_{i+1}.png'), 'PNG')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python pdf2img.py <pdf_file>')
        sys.exit(1)

    pdf_file = sys.argv[1]
    output_directory = os.path.dirname(pdf_file)
    convert_pdf_to_image(pdf_file, output_directory)
