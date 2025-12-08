def main():
    identifyFileType()
    renameFile()
    sortFile()

#set paths to variables
work_path = r"\College"
personal_path = r"\Personal Projects"
unsorted_folder = r"\Users\thuya\Downloads"

def identifyFileType(type_filter):
    {
        type_filter = input("File Extension Requested (comma-separated, leave blank for all):").strip()
        type_filter = {ext.lower().strip().lstrip(".")
            for ext in type_filter.split(",")
            if ext.strip()}
            if type_filter else set()
            }

def renameFile(filename):
    {}

def sortFile(filename):
    {}

if __name__ == '__main__':
    main()