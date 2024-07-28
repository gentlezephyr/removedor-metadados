import piexif
from PIL import Image

from scripts.get_image import select_image


def verificar():
    img = Image.open(select_image())
    exif_dict = {}

    if 'exif' in img.info:
        exif_data = img.info['exif']
        exif_dict = piexif.load(exif_data)

        thumbnail = exif_dict.pop("thumbnail", None)

        if thumbnail is not None:
            with open("easteregg.jpg", "+wb") as f:
                f.write(thumbnail)
                print("Imagem salva com sucesso.")
        else:
            print("Miniatura não encontrada.")

        for ifd_name in exif_dict:
            print(f"\n{ifd_name} IFD:")
            for tag in exif_dict[ifd_name]:
                try:
                    tag_name = piexif.TAGS[ifd_name][tag]["name"]
                    print(f"{tag_name}: {exif_dict[ifd_name][tag]}")
                except KeyError:
                    print(f"Tag {tag}: {exif_dict[ifd_name][tag]}")
    else:
        print("Dados Exif não encontrados.")


if __name__ == '__main__':
    verificar()
