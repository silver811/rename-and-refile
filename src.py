import os
import re
import shutil

def main():
    identifyFileType()
    #select file type
    renameFile() #or press enter to skip
    sortFile()

# Set College Path and Personal Project Path
work_folder = r"/College"
personal_folder = r"\Personal Projects"
unsorted_folder = r"\Users\thuya\Downloads"

#Identify file type
def identifyFileType(type_filter):
    """this is going to identify all files in the parameter
    folder of this file type and return a list of all files

    [well a good chunk of this could be just managed with ls if you're in downloads...
    how about just printing the overall program to be full screen?]
    
    parameters: name of folder to sort through, file suffix
    return: printed string list to terminal"""
    type_filter = input("File Extension Requested (comma-separated, leave blank for all):").strip()
    type_filter = {ext.lower().strip().lstrip(".")
        for ext in type_filter.split(",")
        if ext.strip()}
        if type_filter else set()

#Rename File
def renameFile(filename):
    """take an inputted file name, and assign a new name to it
    make suggestions for naming convention depending on the file sort
    
    [include a way to skip over this command]
    [rename the file with a new number assigned if there is another file with its name in existence]

    parameters: filename
    return: renamed file
    return: File successfully renamed to [new name] OR file name preserved"""
    #allow user to rename file
    print(f"\nFile: {filename}")
    new_base = input(f"Rename base (no extension) or press Enter to keep '{base_name}': ").strip()
    return new_base

#If user provided a new base, check for skip command or sanitize and use it
if new_base:
    if new_base.lower() in {"skip", "s"}:
        print(f"User requested skip for '{filename}', leaving file unchanged.")
        continue
    #append a number to the file if it already exists and assign that to the new file name
    new_base = os.path.splitext(new_base)[0]
    new_base = new_base.replace(os.sep, "_")
    base_name = new_base

def sortFile()
    """use if loops to determine where the file should be placed
    
    parameter: SortingFile variable
    return: string "file successfully moved to [Folder Name]"""

if __name__ == '__main__':
    main()