import os
import json
import tkinter as tk
from tkinter import Button, Toplevel, PhotoImage
import subprocess
from EXE2PNG import EXE2PNG

def launch_exe(path):
    """Function to launch an executable."""
    subprocess.Popen(path, shell=True)

def main():
    # Load JSON data
    with open('setting.json', 'r') as file:
        data = json.load(file)

    # Set up the main window
    root = tk.Tk()
    root.title("Shortcut Panel")

    # For each shortcut in the JSON data, create a button
    for shortcut in data['shortcuts']:
        exe_path = os.path.expandvars(shortcut['path'])  # Handle environment variables in the path
        icon_path = os.path.splitext(os.path.basename(exe_path))[0] + '.png'
        
        # Extract icon if it doesn't exist
        if not os.path.exists(icon_path):
            EXE2PNG(exe_path)

        # Create button with image
        img = PhotoImage(file=icon_path)
        btn = Button(root, text=shortcut['name'], image=img, compound=tk.TOP, 
                     command=lambda exe_path=exe_path: launch_exe(exe_path))
        btn.image = img  # To prevent garbage collection of the image

        # Position button based on position in JSON multiplied by base size
        x, y = shortcut['position']
        btn.grid(row=y, column=x, padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
