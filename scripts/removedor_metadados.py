import piexif
from PIL import Image

from scripts import save_image
from scripts.get_image import select_image


def removedor():
    img = Image.open(select_image())

    if 'exif' in img.info:
        exif_dict = piexif.load(img.info['exif'])
        exif_dict.clear()
        exif_bytes = piexif.dump(exif_dict)
    else:
        exif_bytes = piexif.dump({})

    save_image.save(img, exif_bytes)

    print("Dados apagados com sucesso.")


if __name__ == '__main__':
    removedor()
