# Define paths
$sourceDir = "book1" # Path to your source Markdown files
$tmpDir = "_tmp" # Temporary directory for HTML files
$outputEpub = "output.epub" # The final output EPUB file

# Check if the temporary directory exists, and delete it if it does
if (Test-Path $tmpDir) {
    Remove-Item -Recurse -Force $tmpDir
}

# Create the temporary directory
New-Item -ItemType Directory -Force -Path $tmpDir

# Convert Markdown to HTML
python convert_md_to_html.py -i $sourceDir -o $tmpDir

# Convert HTML to EPUB
python create_epub_from_html.py -i $tmpDir -o $outputEpub

# Cleanup: Remove the temporary directory if you want
if (Test-Path $tmpDir) {
    Remove-Item -Recurse -Force $tmpDir
}