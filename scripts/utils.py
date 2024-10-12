from tkinter import Tk, filedialog

class ImageProcess:
    def __init__(self, img):
        self.img = img

    def save_image(self, exif_bytes):
        root = Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(title="Onde deseja salvar a image?",
                                                 filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")],
                                                 defaultextension=".jpg")

        if file_path:
            self.save(file_path, exif=exif_bytes)
            return file_path

    @staticmethod
    def select_image():
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Selecione uma imagem",
                                               filetypes=[("Imagens", "*.jpg;*.jpeg;*.webp;*.tiff")])

        return file_path