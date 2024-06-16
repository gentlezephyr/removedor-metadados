import piexif
from PIL import Image
from tkinter import Tk, filedialog


def select_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecione uma imagem",
                                           filetypes=[("Imagens", "*.jpg;*.jpeg;*.webp;*.tiff")])
    return file_path


image_path = select_image()

if not image_path:
    print("Nenhuma imagem selecionada.")
else:
    img = Image.open(image_path)

    exif_dict = {}

if 'exif' in img.info:
    exif_data = img.info['exif']
    exif_dict = piexif.load(exif_data)

    thumbnail = exif_dict.pop("thumbnail", None)

    if thumbnail is not None:
        with open("thumbnail.jpg", "+wb") as f:
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
                print(f"{tag_name}: {exif_dict[ifd_name][tag]}")
else:
    print("Dados Exif não encontrados.")
