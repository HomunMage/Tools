import os

# Define the directory to start the recursive search (you can change this to your specific directory)
root_dir = "."

# The string to search for
old_script = '<script src="{{ \'/assets/js/LoadAsCodeSession.js\' | relative_url }}"></script>'

# The string to replace it with
new_script = '<script src="https://posetmage.com/assets/js/LoadAsCodeSession.js"></script>'

def replace_in_file(file_path):
    """Replaces occurrences of old_script with new_script in the given file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Only replace if the old_script is found in the content
        if old_script in content:
            new_content = content.replace(old_script, new_script)
            
            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated: {file_path}")
        else:
            print(f"No changes in: {file_path}")
    
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def replace_in_files_recursively(directory):
    """Recursively traverses the directory and replaces old_script in all files."""
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            replace_in_file(file_path)

# Start the replacement process
replace_in_files_recursively(root_dir)
