import sys
import os
import mutagen
from mutagen import FileType

def get_all_oggs():
    file_list = []
    for dirpath, _, filenames in os.walk(os.getcwd()):
        for file in filenames:
            if file.endswith(".ogg"):
                file_list.append(os.path.abspath(os.path.join(dirpath, file)))
    return file_list

#musicFile = mutagen.File(f'sample/tt_s_ara_dga_trashcan_firstMoveLidFlip3.ogg')
#musicFile = "sample/tt_s_ara_dga_trashcan_firstMoveLidFlip3.ogg"
oggs = get_all_oggs()
formattedFiles = []
for oggFile in oggs:
    print(f"--- {oggFile} ---")
    mFile = mutagen.File(oggFile)
    mFile.tags = None
    if mFile.tags:
        print("Has tags!")
        sys.exit(1)
    # FileType.save(mFile)
    #mFile.save()
    #formattedFiles.append(mFile)
    print(mFile.pprint())
    print()

# for formatFile in formattedFiles:
#     print(f"Saving file {formatFile.info}")
#     formatFile.save()

# print(musicFile.pprint())
