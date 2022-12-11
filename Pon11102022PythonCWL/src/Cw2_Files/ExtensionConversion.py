import os
from pathlib import Path
from PIL import Image

def jpg2png(fullPath):
    for path in fullPath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
            file_extension = path.suffix
            im = Image.open(path)
            newfile_name = path.stem + ".png"#funja with suffix
            print(newfile_name)
            im.save(newfile_name)

def main():
    jpg2png(Path('D:\Semestr7\Python\jpg_files'))

if __name__ == "__main__":
    main()
    
