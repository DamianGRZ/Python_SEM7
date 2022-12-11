import os
from pathlib import Path

def count_files(fullPath):
    count = 0
    for path in fullPath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
                count += 1
        else:
            count = count + count_files(path)
    return count

def main():
    print("Files count:", count_files(Path('D:\Moze przydatne smieci')))

if __name__ == "__main__":
    main()

