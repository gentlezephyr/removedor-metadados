from tkinter import Tk, filedialog


def save(image, exif_bytes):
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(title="Onde deseja salvar a image?",
                                             filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")],
                                             defaultextension=".jpg")

    if file_path:
        image.save(file_path, exif=exif_bytes)
        return file_path
