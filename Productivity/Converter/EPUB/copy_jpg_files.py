import argparse
import os
import shutil
from pathlib import Path

def copy_jpg_files(source_dir, dest_dir):
    source_dir_path = Path(source_dir)
    dest_dir_path = Path(dest_dir)
    
    for root, dirs, files in os.walk(source_dir_path):
        for file in files:
            if file.endswith(".jpg"):
                source_file_path = Path(root) / file
                relative_path = source_file_path.relative_to(source_dir_path)
                dest_file_path = dest_dir_path / relative_path
                
                dest_file_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_file_path, dest_file_path)

def main():
    parser = argparse.ArgumentParser(description="Recursively copy all jpg files from one directory to another.")
    parser.add_argument("-i", "--input", required=True, help="Input directory containing jpg files.")
    parser.add_argument("-o", "--output", required=True, help="Output directory for copied jpg files.")
    
    args = parser.parse_args()
    
    copy_jpg_files(args.input, args.output)

if __name__ == "__main__":
    main()
