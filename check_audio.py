import sys
import os
import mutagen
from mutagen import FileType


# Todo: only checking newly modified files

def get_all_oggs():
    file_list = []
    for dirpath, _, filenames in os.walk(os.getcwd()):
        for file in filenames:
            if file.endswith(".ogg"):
                file_list.append(os.path.abspath(os.path.join(dirpath, file)))
    return file_list


oggs = get_all_oggs()

formattedFiles = []
for oggFile in oggs:
    print(f"--- {oggFile} ---")
    mFile = mutagen.File(oggFile)
    if mFile.tags:
        print("Has tags!")
        sys.exit(1)
    # We will have an option for this later if we wanna figure out how to give proper push perms :p
    mFile.tags = None
    # FileType.save(mFile)
    # mFile.save()
    # formattedFiles.append(mFile)
    print(mFile.pprint())
    print()
