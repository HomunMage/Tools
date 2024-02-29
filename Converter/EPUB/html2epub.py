from ebooklib import epub
import os

def create_epub_from_html(target_dir, output_filename):
    book = epub.EpubBook()
    # Set some basic metadata
    book.set_identifier('id123456')
    book.set_title('Sample Book')
    book.set_language('en')

    # Dictionary to hold the directory structure and corresponding EpubHtml items
    sections = {}

    # Walk through the target directory and add each HTML file to the EPUB
    for root, dirs, files in os.walk(target_dir):
        for file in sorted(files):  # Sort files for consistent order
            if file.endswith('.html') or file.endswith('.md'):
                file_path = os.path.join(root, file)
                section_name = os.path.relpath(root, target_dir)  # Get the relative directory path as section name
                
                # Read the HTML/Markdown content
                with open(file_path, 'r', encoding='utf-8') as content_file:
                    content = content_file.read()

                # For Markdown files, convert to HTML here if necessary
                # e.g., using markdown2 or another library

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

# Example usage
output_epub = 'output.epub'
target_dir = '_tmp'
create_epub_from_html(target_dir, output_epub)
