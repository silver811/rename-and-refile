import os
import shutil
import re

def main():
    formatFileType(type_filter)
    identifyFileType()
    renameFile()
    sortFile()

#set paths to variables
work_path = r"\College"
personal_path = r"\Personal Projects"
unsorted_folder = r"\Users\thuya\Downloads"

type_filter = input("File Extension Requested (comma-separated, leave blank for all):").strip(),

def formatFileType(type_filter):
    #return a formatted list of file extension types
    if type_filter:
        type_filter = {ext.lower().strip().lstrip(".") for ext in type_filter.split(",") if ext.strip()}
    else:
        type_filter = set()

    #return list as extension_list
def identifyFileType(extension_list):
    {
    #find all files in unsorted_folder with the extensions in extension_list
    }

def renameFile(filename):
    """
reassign a new name to a given file
provide note prompting the naming convention for either folder to sort in

college: ####_AssignmenttypeZZZ
personal: XXXX_Projecttype_NameZZZ

include a way to skip over renaming and return the original filename
rename the file with an appended number if there is another file with its name in existence
(ZZZ is the placeholder for where the appended changing number will be)
"""
    print(f"\nFile: {filename}")
    new_base = input(f"Rename base (no extension) or press Enter to keep '{base_name}': ").strip()
    return new_base

#If user provided a new base, check for skip command or sanitize and use it
#probably going to implement this in another function AFTER sorting so file names can be compared
#into compareName you go
if new_base:
    if new_base.lower() in {"skip", "s"}:
        print(f"User requested skip for '{filename}', leaving file name unchanged.")
        continue
    #append a number to the file if it already exists and assign to new file name
    new_base = os.path.splitext(new_base)[0]
    new_base = new_base.replace(os.sep, "_")
    base_name = new_base


def compareName():
    {}

def sortFile(filename):
    {
    """use if to determine where the file should be placed
    
    parameter: file to sort
    return: correctly sorts the file into the folder
    also, return a string like "file successfully sorted into XYZ" or "new file/folder successfully created"
    or whatever else you want happening here..."""
    }

if __name__ == '__main__':
    main()