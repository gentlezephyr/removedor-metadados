import subprocess


def main():
    match_case = int(input("Write 1 to verify, 2 to remove the exif data and 3 to get location: "))

    match match_case:
        case 1:
            print("Verifying!")
            subprocess.run(["python", "scripts/verificador_metadados.py"])
        case 2:
            print("Removing!")
            subprocess.run(["python", "scripts/removedor_metadados.py"])
        case 3:
            print("Locating!")
            subprocess.run(["python", "scripts/localizador.py"])
        case _:
            print("Invalid option!")


if __name__ == '__main__':
    main()
