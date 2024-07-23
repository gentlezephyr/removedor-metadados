from tkinter import Tk, filedialog

root = Tk()

match_case = int(input("Write 1 to verify, 2 to remove the exif data and 3 to get location: "))


def main():
    match match_case:
        case 1:
            print("Verifying!")
            with open("scripts/verificador_metadados.py", "r") as file:
                verify_script = file.read()
            exec(verify_script)
        case 2:
            print("Removing!")
            with open("scripts/removedor_metadados.py", "r") as file:
                remove_script = file.read()
            exec(remove_script)
        case 3:
            print("Locating!")
            with open("scripts/localizador.py", "r") as file:
                locate_script = file.read()
            exec(locate_script)
        case _:
            print("Invalid option!")


if __name__ == '__main__':
    main()
