import piexif
from PIL import Image

img = Image.open("")

if 'exif' in img.info:
    exif_data = img.info['exif']
    exif_dict = piexif.load(exif_data)

for ifd_name in exif_dict:
    print(f"\n{ifd_name} IFD:")
    for tag in exif_dict[ifd_name]:
        tag_name = piexif.TAGS[ifd_name][tag]["name"]
        print(f"{tag_name}: {exif_dict[ifd_name][tag]}")

else:
    print("Não há metadados EXIF na imagem.")

