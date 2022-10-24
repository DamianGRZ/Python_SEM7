import os
from pathlib import Path
from PIL import Image

def count_files(fullPath):
    count = 0
    for path in fullPath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
                count += 1
        else:
            count = count + count_files(path)
    return count

def rec_show_trunk(startPath, indentation):
    indentation += 1
    for path in startPath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
            print(indentation*" ", path)
        else:
            rec_show_trunk(path, indentation)


def jpg2png(fullPath):
    for path in fullPath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
            file_extension = path.suffix
            im = Image.open(path)
            newfile_name = path.stem + ".png"#funja with suffix
            print(newfile_name)
            im.save(newfile_name)

#EX2
if __name__ == "__main__":#uruchamianie oddzielne zadania
    ##Count files
    #print("----------------------------------------------------------")
    #print("Ex2.1, Count files:")
    #print("Files count:", count_files(Path('D:\Semestr7\Python')))

    ## Directory structure
    #print("----------------------------------------------------------")
    #print("Ex2.2, Directory structure:")
    #indentation = 0
    #rec_show_trunk(Path('D:\Semestr7'), indentation)
    
    # Count files
    print("----------------------------------------------------------")
    print("Ex2.3, File conversion from jpg to png:")
    jpg2png(Path('D:\Semestr7\Python\jpg_files'))