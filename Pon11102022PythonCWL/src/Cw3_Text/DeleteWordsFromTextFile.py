import os
from pathlib import Path
#timeit lub timePerformanceTimer

def Delete_words(words_to_delete, data):
    for excluded in words_to_delete:
        newlines = []
        for line in data:
            newline = ""
            for word in line.split():
                if word == excluded:
                    continue
                else:
                    newline = newline + word + " "
            #Remove leading and trailing spaces using strip()
            newline.strip()  # | for OR condition #taka sama func str.strip()
            newlines.append(newline)
        data = newlines
    return newlines


def Save_to_file(fullPath, lines, fileName):
    completeName = os.path.join(os.path.dirname(fullPath), fileName) 
    with open(completeName, 'w') as outfile:
        for line in lines:
            outfile.write("{}\n".format(line))

def Read_from_file(path):
    with open(path, encoding = 'utf-8') as f:
        return f.readlines()

def Check_if_good_file(path):
    if os.path.isfile(path):
        file_extension = path.suffix
        #check if file is txt files
        if file_extension == ".txt":
            return True
        else:
            return False

def delete_silver_word(fpath):
    excludedWords = ["Sie", "oraz", "i", "dlaczego", "nigdy"]
    for path in fpath.glob('*'):
        if Check_if_good_file(path):
            lines = Read_from_file(path)
            new_lines = Delete_words(excludedWords, lines)
            Save_to_file(path, new_lines, "Excluded.txt")

def main():
    delete_silver_word(Path('D:\Semestr7\Python'))

if __name__ == "__main__":
    main()
