from ebooklib import epub
import os
import mimetypes
import argparse

mimetypes.add_type('image/webp', '.webp')

def create_epub_from_html(target_dir, output_filename):
    book = epub.EpubBook()
    # Set some basic metadata
    book.set_identifier('id123456')
    book.set_title('鍊金魔法師 - 創業xAIx學習')
    book.set_language('en')

    # Dictionary to hold the directory structure and corresponding EpubHtml items
    sections = {}

    # Hold a list of added images to avoid duplicates
    added_images = {}

    # Walk through the target directory and add each HTML/Markdown file and images to the EPUB
    for root, dirs, files in os.walk(target_dir):
        for file in sorted(files):  # Sort files for consistent order
            file_path = os.path.join(root, file)
            if file.endswith('.html') or file.endswith('.md'):
                section_name = os.path.relpath(root, target_dir)  # Get the relative directory path as section name

                # Read the HTML/Markdown content
                with open(file_path, 'r', encoding='utf-8') as content_file:
                    content = content_file.read()

                # Create an EPUB item for this file
                epub_item = epub.EpubHtml(title=os.path.splitext(os.path.basename(file))[0],
                                          file_name=file.replace(os.path.sep, '_'),  # Ensure unique filenames
                                          content=content)
                book.add_item(epub_item)

                # Organize items into sections based on their directory
                if section_name not in sections:
                    sections[section_name] = []
                sections[section_name].append(epub_item)

                # Add the item to the book's spine
                book.spine.append(epub_item)

            elif file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                # Ensure we don't add the same image multiple times
                if file not in added_images:
                    mime_type, _ = mimetypes.guess_type(file_path)
                    if mime_type:  # Only proceed if a valid mime type is found
                        epub_image = epub.EpubImage()
                        epub_image.file_name = os.path.join('Images', file.replace(os.path.sep, '_'))
                        epub_image.media_type = mime_type
                        with open(file_path, 'rb') as img_file:
                            epub_image.content = img_file.read()
                        book.add_item(epub_image)
                        added_images[file] = epub_image.file_name
                        # Note: You'll need to update your HTML content to reference these images correctly
                        print(f"Adding image: {file_path} as {epub_image.file_name}")

    # Create a hierarchical TOC and sections for the book
    toc_list = []
    for section_name, items in sections.items():
        if section_name == '.':  # Top-level files
            toc_list.extend(items)
        else:
            # Create a subsection for nested directories
            section_title = section_name.replace(os.path.sep, ' / ')  # Use directory path as section title
            toc_list.append((epub.Section(section_title), items))

    book.toc = toc_list

    # Add necessary navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Write the EPUB file
    epub.write_epub(output_filename, book, {})

def main():
    parser = argparse.ArgumentParser(description='Create an EPUB file from HTML or Markdown files in a directory, including images.')
    parser.add_argument('-i', '--input', required=True, help='Input directory containing HTML or Markdown files and images.')
    parser.add_argument('-o', '--output', required=True, help='Output EPUB file name.')

    args = parser.parse_args()

    create_epub_from_html(args.input, args.output)

if __name__ == '__main__':
    main()
