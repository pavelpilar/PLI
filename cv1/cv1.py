from math import log2 as log, sin, cos
import pathlib
import re

for file in list(pathlib.Path().glob('*.txt')):
    for line in file.open().read().splitlines():

        match = re.search("^([\w\d\+\-*/\(\)]+) ?= ?(\d+)$", line)
        if match is not None:
            groups = match.groups()
            
            print(line + " : " + ("Správně" if int(eval(groups[0])) == int(groups[1]) else "Špatně"))
