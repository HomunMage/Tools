# PDF2Image 

## PDF2Image by python

<div class="load_as_code_session" data-url="pdf2img.py">
  Loading content...
</div>


## PDF2Image by CLI

To convert each page of a PDF into separate image files using a CLI (Command Line Interface) tool, you can use **`pdftoppm`**, part of the `poppler-utils` package, or **`ImageMagick`**. Here are solutions using both:

---

### **Option 1: Using `pdftoppm`**
1. **Install `poppler-utils`** (if not installed):
   - On Debian/Ubuntu:  
     ```bash
     sudo apt update
     sudo apt install poppler-utils
     ```
   - On macOS (via Homebrew):  
     ```bash
     brew install poppler
     ```

2. **Convert PDF to Images**:
   ```bash
   pdftoppm -png input.pdf output
   ```
   - `-png`: Sets the output format to PNG (use `-jpeg` for JPEG).
   - `input.pdf`: The input PDF file.
   - `output`: The prefix for output image files (e.g., `output-1.png`, `output-2.png`).

---

### **Option 2: Using ImageMagick**
1. **Install ImageMagick**:
   - On Debian/Ubuntu:  
     ```bash
     sudo apt update
     sudo apt install imagemagick
     ```
   - On macOS (via Homebrew):  
     ```bash
     brew install imagemagick
     ```

2. **Convert PDF to Images**:
   ```bash
   convert -density 300 input.pdf page-%03d.png
   ```
   - `-density 300`: Sets resolution to 300 DPI (higher values produce better quality images).
   - `input.pdf`: The input PDF file.
   - `page-%03d.png`: Output filenames with a three-digit page number (e.g., `page-001.png`, `page-002.png`).

---

### **Advanced Options**
- To extract specific pages with `pdftoppm`, use the `-f` (from) and `-l` (last) flags:
  ```bash
  pdftoppm -png -f 2 -l 5 input.pdf output
  ```
  This converts pages 2 to 5 only.

- To customize image size or quality in `ImageMagick`:
  ```bash
  convert -density 300 -quality 90 input.pdf page-%03d.png
  ```
  - `-quality 90`: Sets the compression quality for JPEG/PNG output.

Both tools are efficient and widely available on Linux, macOS, and Windows (via WSL or binaries). Let me know if you need further assistance!



<script src="https://posetmage.com/assets/js/LoadAsCodeSession.js"></script>