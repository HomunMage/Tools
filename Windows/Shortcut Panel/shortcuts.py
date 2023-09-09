
import os
import json
import tkinter as tk
from tkinter import Button, Toplevel, PhotoImage
import subprocess

def launch_exe(path):
    """Function to launch an executable."""
    subprocess.Popen(path, shell=True)

def main():
    # Load JSON data
    with open('setting.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Set up the main window
    root = tk.Tk()
    root.title("Shortcut Panel")

    basesize = data['basesize']  # Load basesize from JSON

    # For each shortcut in the JSON data, create a button
    for shortcut in data['shortcuts']:
        exe_path = os.path.expandvars(shortcut['path'])  # Handle environment variables in the path
        
        # Check if "icon" field exists, otherwise use the default naming scheme
        icon_path = shortcut.get('icon', None)
        if not icon_path:
            icon_path = os.path.splitext(os.path.basename(exe_path))[0] + '.png'

        # Create button with image
        img = PhotoImage(file=icon_path)
        
        # Resize the image based on basesize and shortcut's size
        size_multiplier = shortcut['size']
        new_width = basesize * size_multiplier
        new_height = basesize * size_multiplier

        img = img.subsample(int(img.width() // new_width), int(img.height() // new_height))
        
        # Create the button with the adjusted width, height, and no text
        btn = Button(root, image=img, compound=tk.TOP, 
                     command=lambda exe_path=exe_path: launch_exe(exe_path))
        btn.image = img  # To prevent garbage collection of the image

        # Calculate rowspan and columnspan based on shortcut size
        rowspan = columnspan = shortcut['size']

        # Position button based on position in JSON, and account for rowspan/columnspan
        x, y = shortcut['position']
        btn.grid(row=y, column=x, padx=5, pady=5, rowspan=rowspan, columnspan=columnspan)

    root.mainloop()

if __name__ == '__main__':
    main()
