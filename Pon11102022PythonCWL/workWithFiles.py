import os
from pathlib import Path
from PIL import Image

def count_files(fullPath):
    count = 0
    for path in os.listdir(fullPath):
        # check if current path is a file
        if os.path.isfile(os.path.join(fullPath, path)):
            count += 1
    return count

def rec_show_trunk(startPath, indentation):

    for path in startPath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
            print(indentation*" ", path)
        else:
            indentation += 1
            rec_show_trunk(path, indentation)


def jpg2png(fullPath):
    for path in fullPath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
            file_extension = path.suffix
            if file_extension == ".jpg":
                im = Image.open(path)
                newfile_name = path.stem + ".png"
                print(newfile_name)
                im.save(newfile_name)
