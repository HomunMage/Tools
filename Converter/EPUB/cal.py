import os
import re

# Directory path
directory_path = './'  # Assuming files are in the /mnt/data directory for this environment

# Regular expression to match Chinese characters
chinese_char_pattern = re.compile(r'[\u4e00-\u9fff]')

# Counter for Chinese characters
chinese_char_count = 0

# Using os.walk() to recursively visit all directories, subdirectories and files
for root, dirs, files in os.walk(directory_path):
    for filename in files:
        # Check if the file is a Markdown file
        if filename.endswith('.md'):
            # Construct the full path to the file
            file_path = os.path.join(root, filename)
            # Open and read the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Find all Chinese characters in the content
                chinese_chars = chinese_char_pattern.findall(content)
                # Update the count
                chinese_char_count += len(chinese_chars)
                print("file:", filename, "words", len(chinese_chars))


print("Total number of Chinese words in .md files:", chinese_char_count)
