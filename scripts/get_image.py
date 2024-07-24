from tkinter import Tk, filedialog


def select_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecione uma imagem",
                                           filetypes=[("Imagens", "*.jpg;*.jpeg;*.webp;*.tiff")])

    return file_path


if __name__ == '__main__':
    print(select_image())
