import os
import shutil
import re

def main():

    # ask for filters
    type_filter = formatFileType()
    name_filter = input("Filter by name contains (leave blank for all): ").strip().lower()

    # identify candidate files
    matches = identifyFileType(type_filter, name_filter)
    for filename, base_name, file_ext in matches:
        source_path = os.path.join(unsorted_folder, filename)

        # file renaming
        updated_base = renameFile(filename, base_name)
        # skip if requested
        if updated_base is None:
            continue

        # sort files
        sortFile(source_path, updated_base, file_ext)

# set paths to variables
work_path = r"\College"
personal_path = r"\Personal Projects"
unsorted_folder = r"\Users\thuya\Downloads"


def formatFileType():
    """
    Ask user for a comma-separated list of extensions and
    returns extension strings without dots.
    """

    # filter by file type
    type_filter_str = input("Filter by extensions (comma-separated, leave blank for all): ").strip()

    # return file type set
    if type_filter_str:
        exts = []
        for ext in type_filter_str.split(","):
            cleaned = ext.strip().lower().lstrip(".")
            if cleaned:
                exts.append(cleaned)
        return exts if exts else None
    else:
        return None


def identifyFileType(type_filter, name_filter):
    """
    Find all files that match the filters with the name+extension, name, and extension.
    """
    # create matches list
    matches = []

    # process each file in downloads
    for filename in sorted(os.listdir(unsorted_folder)):
        source_path = os.path.join(unsorted_folder, filename)

        # Skip directories
        if not os.path.isfile(source_path):
            continue

        # separate file into its name and filetype
        base_name, filetype = os.path.splitext(filename)
        file_ext = filetype
        ext = filetype.lstrip(".").lower()

        # extension filter
        if type_filter and ext not in type_filter:
            continue

        # name filter
        if name_filter and name_filter not in filename.lower():
            continue

        # add to matches list
        matches.append((filename, base_name, file_ext))

    return matches


def renameFile(filename, base_name):
    """
    Reaneme files to sort.
    """

    # input for rename
    print(f"\nFile: {filename}")
    new_base = input(f"Work Naming Convention: FOLDERNAME_FILENAMEPART\nPersonal Project Naming Convention: PROJECTFOLDER_TYPE_NAME\nRename base (no extension) or press Enter to keep '{base_name}': ").strip()

    # check for skip command
    if new_base:
        if new_base.lower() in {"skip", "s"}:
            print(f"User requested skip for '{filename}', leaving file unchanged.")
            return None

        # create path with name
        new_base = new_base.replace(os.sep, "_")
        base_name = new_base

    return base_name


def compareName(destination_dir, dest_base, file_ext):
    """
    Determine the next available numbered of files with the same name.
    """
    
    # list existing files in the destination directory
    existing = os.listdir(destination_dir)
    #use base name, and then append the file extension
    pattern = re.compile(rf"^{re.escape(dest_base)}_(\d{{3}}){re.escape(file_ext)}$", re.IGNORECASE)

    # extract existing numbers
    numbers = [int(m.group(1)) for m in (pattern.search(f) for f in existing) if m]
    next_number = max(numbers) + 1 if numbers else 1

    # build a filename and make sure it doesn't already exist
    while True:
        new_name = f"{dest_base}_{next_number:03d}{file_ext}"
        destination_path = os.path.join(destination_dir, new_name)
        if not os.path.exists(destination_path):
            return new_name
        next_number += 1


def sortFile(source_path, base_name, file_ext):
    """
    Decide where the file should go and move it with the correct naming convention.

    Work projects:
        base: FOLDERNAME_FILENAMEPART
        Folder: work_path / FOLDERNAME
        File:  FILENAMEPART_NNN.ext

    Personal projects:
        base: PROJECTFOLDER_TYPE_NAME
        Folder: personal_path / PROJECTFOLDER
        File:   TYPE_NAME_NNN.ext
    """

    # count underscores to determine where to sort
    underscore_count = base_name.count("_")

    # work projects sorting (one underscore, two parts)
    if underscore_count == 1:
        parts = base_name.split("_", 1)
        foldername = parts[0]
        filename_part = parts[1]

        destination_dir = os.path.join(work_path, foldername)
        os.makedirs(destination_dir, exist_ok=True)

        dest_base = filename_part

    # personal projects sorting
    elif underscore_count == 2:

        # split into three parts only
        parts = base_name.split("_", 2)
        foldername_in_projects = parts[0]
        type_part = parts[1]
        name_part = parts[2]

        # make destination directory
        destination_dir = os.path.join(personal_path, foldername_in_projects)
        os.makedirs(destination_dir, exist_ok=True)
        dest_base = f"{type_part}_{name_part}"

    else:
        print(f"Skipping '{os.path.basename(source_path)}': ")
        print(f"underscore count {underscore_count}. ")
        print("It needs to be 1 (work) or 2 (personal) to sort properly.")

    # determine unique filename
    new_name = compareName(destination_dir, dest_base, file_ext)
    destination_path = os.path.join(destination_dir, new_name)

    # move the file
    shutil.move(source_path, destination_path)
    print(f"Moved {os.path.basename(source_path)} -> {destination_path}")

if __name__ == "__main__":
    main()