import piexif
from PIL import Image
from tkinter import Tk, filedialog


def select_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecione uma imagem",
                                           filetypes=[("Imagens", "*.jpg;*.jpeg;*.webp;*.tiff")])
    return file_path


def save_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(title="Onde deseja salvar a image?", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")], defaultextension=".jpg")

    return file_path


img = Image.open(select_image())

if 'exif' in img.info:
    exif_dict = piexif.load(img.info['exif'])
    exif_dict.clear()
    exif_bytes = piexif.dump(exif_dict)
else:
    exif_bytes = piexif.dump({})

image_path = save_image()

img.save(image_path)

print("Dados apagados com sucesso.")