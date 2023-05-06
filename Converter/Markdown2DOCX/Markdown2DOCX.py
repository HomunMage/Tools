import subprocess
import sys
import os
import shutil
import argparse
import re
import markdown
import pypandoc

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Process input file and output folder')

# Add arguments to the parser
parser.add_argument('-i', '--input', type=str, required=True, help='Input file path')
parser.add_argument('-of', '--output_folder', type=str, required=True, help='Output folder path')

# Parse the command-line arguments
args = parser.parse_args()

input_file = args.input

output_folder = f"{args.output_folder}/"
output_mermaid_folder = f"{output_folder}/mermaid/"
output_file = f"{output_mermaid_folder}/diag.png"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if not os.path.exists(output_mermaid_folder):
    os.makedirs(output_mermaid_folder)

mmdc_path = shutil.which("mmdc")
if mmdc_path is not None:
    subprocess.check_call([mmdc_path, "-i", input_file, "-o", output_file])
else:
    print("mmdc not found in PATH")

# Read the temp.md file
with open(input_file, "r", encoding="utf-8") as file:
    file_content = file.read()

# Find all Mermaid code blocks
mermaid_blocks = re.findall(r'```mermaid([\s\S]*?)```', file_content)

# Replace Mermaid blocks with image links
count = 1
for block in mermaid_blocks:
    file_content = file_content.replace(f"```mermaid{block}```", f"![](./mermaid/diag-{count}.png)")
    count += 1

# Convert the Markdown content to HTML
html_content = markdown.markdown(file_content, extensions=["tables", "fenced_code", "nl2br"])

input_html_file = f"{output_folder}/output.html"
# Save the HTML content to the output file
with open(input_html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

# Print success message
print(f"Input file '{input_file}' processed and converted to '{input_html_file}' successfully.")

output_docx_file = f"{output_folder}/output.docx"
output = pypandoc.convert_file(input_html_file, 'docx', outputfile=output_docx_file)

# Print a message if the conversion was successful
if output == '':
    print(f'Successfully converted {input_html_file} to {output_docx_file}')
else:
    print('Conversion failed')

