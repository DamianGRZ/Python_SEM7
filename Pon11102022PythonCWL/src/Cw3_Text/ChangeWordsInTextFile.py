import os
from pathlib import Path
#timeit lub timePerformanceTimer

def change_silver_word(fpath):
    changeWords = {
    "i": "oraz",
    "oraz":"i",
    "nigdy": "prawie nigdy",
    "dlaczego": "czemu"
    }
    for path in fpath.glob('*'):
        if Check_if_good_file(path):
            lines = Read_from_file(path)
            new_lines = Change_words(changeWords, lines)
            Save_to_file(path, new_lines, "Changed.txt")

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

def Change_words(words_to_change, data):
    newlines = []
    for line in data:
        newline = ""
        for word in line.split():
            change_flag = 0
            for change_word in words_to_change:
                if word == change_word:
                    newline = newline + words_to_change[change_word] + " "
                    change_flag = 1
                    continue
            if change_flag == 0:
                newline = newline + word + " "
        newline.strip()
        newlines.append(newline)
    return newlines

def main():
    change_silver_word(Path('D:\Semestr7\Python'))

if __name__ == "__main__":
    main()
