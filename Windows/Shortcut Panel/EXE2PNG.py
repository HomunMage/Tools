import os
from PIL import Image
import icoextract

def EXE2PNG(exe_path):
    # Extract filename without extension from the file path
    base_name = os.path.basename(exe_path)  # gets filename with extension
    filename_without_extension = os.path.splitext(base_name)[0]
    save_path = os.path.join(filename_without_extension + '.png')
    ico_path = os.path.join(filename_without_extension + '.ico')
    
    # Check if the given path exists
    if not os.path.exists(exe_path):
        print(f"File not found: {exe_path}")
        return

    # Extract icon from the EXE
    ie = icoextract.IconExtractor(exe_path)
    icons = ie.list_group_icons()
    if icons:
        # Save to a temporary ICO file
        ie.export_icon(ico_path, 0)  # Using 0 as an index for the first icon

        img = Image.open(ico_path)
        img.save(save_path)

        print(f"Icon saved to {save_path}")
    else:
        print(f"No icons found in {exe_path}")

if __name__ == "__main__":
    exe_path = os.path.expandvars("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    EXE2PNG(exe_path)
