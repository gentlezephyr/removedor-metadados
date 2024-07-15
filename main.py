from tkinter import Tk, filedialog

root = Tk()

match_case = int(input("Write 1 to verify or 2 to remove the exif data!"))


def main():
    match match_case:
        case 1:
            print("Verifying!")
            with open("verificador_metadados.py", "r") as file:
                verify_script = file.read()
            exec(verify_script)
        case 2:
            print("Removing!")
            with open("removedor_metadados.py", "r") as file:
                remove_script = file.read()
            exec(remove_script)
        case _:
            print("Invalid option!")


if __name__ == '__main__':
    main()
