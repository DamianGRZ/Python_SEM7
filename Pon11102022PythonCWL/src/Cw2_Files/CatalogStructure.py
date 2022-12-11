import os
from pathlib import Path

def rec_show_trunk(startPath, indentation):
    indentation += 1
    for path in startPath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
            print(indentation*" ", path)
        else:
            rec_show_trunk(path, indentation)

def main():
    indentation = 0
    rec_show_trunk(Path('D:\Semestr7'), indentation)

if __name__ == "__main__":
    main()
