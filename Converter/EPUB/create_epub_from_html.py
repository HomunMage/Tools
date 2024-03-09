from ebooklib import epub
import os
import mimetypes
import uuid
import argparse
import pypandoc

def create_toc_page(sections):
    """Generate TOC HTML content."""
    toc_content = '<h1>Table of Contents</h1>'
    for section_name, items in sections.items():
        if section_name != '.':
            toc_content += f'<h2>{section_name}</h2>'
        toc_content += '<ul>'
        for item in items:
            toc_content += f'<li>{item.title}</li>'
        toc_content += '</ul>'
    return toc_content

def create_epub_from_html(target_dir, output_filename):
    book = epub.EpubBook()
    # Set some basic metadata

    unique_id = str(uuid.uuid4())
    book.set_identifier(unique_id)

    book.set_title('鍊金Mage - 創業思維x人工智慧x學習技巧')
    book.add_author('鍊金Mage')
    book.set_language('zh-tw')

    cover_image_path = os.path.join(target_dir, 'cover.jpg')
    mime_type, _ = mimetypes.guess_type(cover_image_path)
    if mime_type:
        with open(cover_image_path, 'rb') as img_file:
            book.set_cover("cover.jpg", img_file.read(), create_page=True)

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

                print(f"Adding file: {file_path}")

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

    # Generate and add TOC page
    toc_content = create_toc_page(sections)
    toc_page = epub.EpubHtml(title='Table of Contents', file_name='toc.html', content=toc_content, lang='en')
    book.add_item(toc_page)
    book.spine.insert(0, toc_page)  # Insert TOC at the beginning of the spine

    # Create a hierarchical TOC and sections for the book
    toc_list = [(epub.Section('Table of Contents'), [toc_page])]
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
