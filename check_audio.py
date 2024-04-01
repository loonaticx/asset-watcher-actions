import sys
import mutagen
from mutagen import FileType


#musicFile = mutagen.File(f'sample/tt_s_ara_dga_trashcan_firstMoveLidFlip3.ogg')
musicFile = "sample/tt_s_ara_dga_trashcan_firstMoveLidFlip3.ogg"
oggs = [musicFile]
formattedFiles = []
for oggFile in oggs:
    print(f"--- {oggFile} ---")
    mFile = mutagen.File(oggFile)
    #mFile.tags = None
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
