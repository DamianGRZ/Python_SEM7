from calendar import c
import os
from pathlib import Path
from PIL import Image
import workWithFiles
import random
import inout
import text
import Classes
import math
import Calculations_and_algorithms
import numpy as np
import xml.sax
import xml.dom

def parse_sax(fpath):
    for path in fpath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
            file_extension = path.suffix
            #check if file is txt files
            if file_extension == ".xml":
                 parser = xml.sax.make_parser()
                 lines = parser.parse(path)
                 for elem in lines.findall("Employee/SSN"):
                    elem.tag = "EESSN"
                 completeName = os.path.join(os.path.dirname(path), os.path.basename(path)+"excluded.txt") 
                 lines.write(completeName)


#EX6
if __name__ == "__main__":
    #parse_sax(Path('D:\Semestr7\Python'))
    x = 1