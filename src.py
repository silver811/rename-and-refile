"""Take files from any software on the PC and
ensure proper naming convention that can be set,
then place it in the proper folder.

 1. Read the file name and type
 2. Ask what folder it needs to be sorted into
 3. Read the names of other files within that folder, and match the naming convention numerically
 4. Update file placement when the name of a file is updated
 5. Filtering system by file name and type

  ideally, this project will be able to interface with OBS,
  Obsidian, browser  Downloads, Maya, Adobe, and Clip Studio Paint
"""
import shutil
import os

unsorted_folder = "C:\Users\thuya\Downloads"
work_folder_path = "C:\College"
project_folder_path = "C:\Personal Projects"

for filename in os.listdir(unsorted_folder):
    path, filetype = os.path.splitext(filename)
    filename_category = filename.split("_")
    folder_location = filename_category[0]
    try:
        os.mkdir(f"{filetype}")
    except:
        print(f"Folder for {filetype} exists")
    shutil.move(unsorted_folder, f"{project_folder_path}/{folder_location}/{filetype}")
