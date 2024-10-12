import piexif
from PIL import Image
from utils import ImageProcess


def localizador():
    image_process = ImageProcess
    img_filepath = image_process.select_image()
    img = Image.open(img_filepath)
    exif_dict = {}

    if 'exif' in img.info:
        exif_data = img.info['exif']
        exif_dict = piexif.load(exif_data)

        thumbnail = exif_dict.pop("thumbnail", None)

    gps_info = None

    if "GPS" in exif_dict:
        gps_info = exif_dict["GPS"]
        for tag in gps_info:
            tag_name = piexif.TAGS["GPS"][tag]["name"]
            print(f"{tag_name}: {gps_info[tag]}")

    if gps_info:
        latitude, longitude = get_decimal_coordinates(gps_info)
        latitude_dms = decimal_to_dms(latitude, is_latitude=True)
        longitude_dms = decimal_to_dms(longitude, is_latitude=False)
        print(f"Latitude: {latitude_dms}")
        print(f"Longitude: {longitude_dms}")
    else:
        print("Não foram encontrados dados de GPS na imagem.")


def convert_to_decimal(degrees, minutes, seconds):
    return degrees + (minutes / 60) + (seconds / 3600)


def get_decimal_coordinates(gps_data):
    # Latitude
    latitude: list = gps_data[2]
    latitude_ref = gps_data[1].decode('utf-8')
    latitude_degrees = latitude[0][0] / latitude[0][1]
    latitude_minutes = latitude[1][0] / latitude[1][1]
    latitude_seconds = latitude[2][0] / latitude[2][1]
    latitude_decimal = convert_to_decimal(latitude_degrees, latitude_minutes, latitude_seconds)
    if latitude_ref == 'S':
        latitude_decimal = -latitude_decimal

    # Longitude
    longitude: list = gps_data[4]
    longitude_ref = gps_data[3].decode('utf-8')
    longitude_degrees = longitude[0][0] / longitude[0][1]
    longitude_minutes = longitude[1][0] / longitude[1][1]
    longitude_seconds = longitude[2][0] / longitude[2][1]
    longitude_decimal = convert_to_decimal(longitude_degrees, longitude_minutes, longitude_seconds)
    if longitude_ref == 'W':
        longitude_decimal = -longitude_decimal

    return latitude_decimal, longitude_decimal


def decimal_to_dms(decimal, is_latitude):
    is_positive = decimal >= 0
    decimal = abs(decimal)
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = (decimal - degrees - minutes / 60) * 3600

    direction = ''
    if is_latitude:
        direction = 'N' if is_positive else 'S'
    else:
        direction = 'E' if is_positive else 'W'

    return f"{degrees}°{minutes}'{seconds:.1f}\"{direction}"


if __name__ == '__main__':
    localizador()
