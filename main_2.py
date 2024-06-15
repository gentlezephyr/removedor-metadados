import piexif
from PIL import Image

img = Image.open("")

if 'exif' in img.info:
    exif_dict = piexif.load(img.info['exif'])
    exif_dict.clear()
    exif_bytes = piexif.dump(exif_dict)
else:
    exif_bytes = piexif.dump({})

img.save('', 'jpeg', exif=exif_bytes)
