from ebooklib import epub
import os

def create_epub_from_html(target_dir, output_filename):
    book = epub.EpubBook()
    # Set some basic metadata
    book.set_identifier('id123456')
    book.set_title('Sample Book')
    book.set_language('en')

    # Walk through the target directory and add each HTML file to the EPUB
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                # Read the HTML content
                with open(file_path, 'r', encoding='utf-8') as html_file:
                    html_content = html_file.read()

                # Create an EPUB item for this file
                epub_item = epub.EpubHtml(title=file.replace('.html', ''), file_name=file, content=html_content)
                book.add_item(epub_item)

                # Add the item to the book's spine
                book.spine.append(epub_item)

    # Define EPUB TOC and spine
    book.toc = (epub.Link(file, os.path.basename(file).replace('.html', ''), os.path.basename(file).replace('.html', '')) for file in os.listdir(target_dir) if file.endswith('.html'))
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Write the EPUB file
    epub.write_epub(output_filename, book, {})

# Example usage
output_epub = 'output.epub'
target_dir = '_tmp'
create_epub_from_html(target_dir, output_epub)
