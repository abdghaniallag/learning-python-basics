#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile
def main():
    # make a duplicate of an existing file
    if path.exists("newtextfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("newtextfile.txt")
        # let's make a backup copy by appending "bak" to the name
        #destination= src+".bak"
        #shutil.copy(src,destination)
        # rename the original file
        #os.rename("textfile.txt","newtextfile.txt")
        # now put things into a ZIP archive
        # root_dir, tail =path.split(src)
        # make_archive("archive","zip", root_dir)
        # more fine-grained control over ZIP files
        with ZipFile("zipfile.zip","w") as zip:
            zip.write("newtextfile.txt")
            zip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()
