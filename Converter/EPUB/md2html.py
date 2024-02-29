import os
import pypandoc

def convert_md_to_html(source_dir, target_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.md'):
                # Define the source and target paths
                md_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_dir)
                target_path = os.path.join(target_dir, relative_path)
                os.makedirs(target_path, exist_ok=True)
                html_filename = file.replace('.md', '.html')
                html_path = os.path.join(target_path, html_filename)
                
                # Convert Markdown to HTML
                html_content = pypandoc.convert_file(md_path, 'html')
                
                # Write the HTML content to the target directory
                with open(html_path, 'w', encoding='utf-8') as html_file:
                    html_file.write(html_content)

# Example usage
source_dir = 'book1'
target_dir = '_tmp'
convert_md_to_html(source_dir, target_dir)