import os
import re
from pathlib import Path

def delete_silver_word(fpath):
    excludedWords = ["Sie", "oraz", "i", "dlaczego", "nigdy"]
    for path in fpath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
            file_extension = path.suffix
            #check if file is txt files
            if file_extension == ".txt":
                with open(path, encoding = 'utf-8') as f:
                    lines = f.readlines()      
                    for excluded in excludedWords:
                        newlines = []
                        for line in lines:
                            newline = ""
                            for word in line.split():
                                if word == excluded:
                                    continue
                                else:
                                    newline = newline + " " + word
                            #Remove leading and trailing spaces using RegEx
                            newline = re.sub(r"^\s+|\s+$", "", newline)  # | for OR condition
                            newlines.append(newline)
                        lines = newlines
                    #save to file
                    completeName = os.path.join(os.path.dirname(path), "excluded.txt") 
                    with open(completeName, 'w') as outfile:
                        for line in lines:
                            outfile.write("{}\n".format(line))

def change_silver_word(fpath):
    changeWords = {
    "i": "oraz",
    "oraz":"i",
    "nigdy": "prawie nigdy",
    "dlaczego": "czemu"
    }
    for path in fpath.glob('*'):
    # check if current path is a file
        if os.path.isfile(path):
            file_extension = path.suffix
            #check if file is txt files
            if file_extension == ".txt":
                with open(path, encoding = 'utf-8') as f:
                    lines = f.readlines()   
                    newlines = []
                    for line in lines:
                        newline = ""
                        for word in line.split():
                            change_flag = 0
                            for change_word in changeWords:
                                if word == change_word:
                                    newline = newline + " " + changeWords[change_word]
                                    change_flag = 1
                                    continue
                            if change_flag == 0:
                                newline = newline + " " + word
                        #Remove leading and trailing spaces using RegEx
                        newline = re.sub(r"^\s+|\s+$", "", newline)  # | for OR condition
                        newlines.append(newline)
                    lines = newlines
                    #save to file
                    completeName = os.path.join(os.path.dirname(path), "changed.txt") 
                    with open(completeName, 'w') as outfile:
                        for line in lines:
                            outfile.write("{}\n".format(line))

#EX3
if __name__ == "__main__":
    delete_silver_word(Path('D:\Semestr7\Python'))
    change_silver_word(Path('D:\Semestr7\Python'))