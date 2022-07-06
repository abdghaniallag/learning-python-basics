
import os
from os import path

totalbytecount = 0

listoffiles = os.listdir()
for file in listoffiles:
    if path.isfile(file):
        totalbytecount += os.path.getsize(file)

os.mkdir("results")
results = open("results/results.txt", "w+")
if results.mode == "w+":
    results.write("Total bytecount:" + str(totalbytecount) + "\n")
    results.write("Files list:\n")
    results.write("--------------\n")
    for file in listoffiles:
        if os.path.isfile(file):
            results.write(file + "\n")
    results.close()
