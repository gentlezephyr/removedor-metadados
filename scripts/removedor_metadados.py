import piexif
from PIL import Image
from utils import ImageProcess


def removedor():
    image_process = ImageProcess
    img_path = image_process.select_image()
    img = Image.open(img_path)

    if 'exif' in img.info:
        exif_dict = piexif.load(img.info['exif'])
        exif_dict.clear()
        exif_bytes = piexif.dump(exif_dict)
    else:
        exif_bytes = piexif.dump({})

    image_process.save_image(img, exif_bytes)

    print("Dados apagados com sucesso.")


if __name__ == '__main__':
    removedor()
