import piexif
from PIL import Image

from scripts.get_image import image_path


def localizador():

    img = Image.open(image_path)
    exif_dict = {}

    if 'exif' in img.info:
        exif_data = img.info['exif']
        exif_dict = piexif.load(exif_data)

        thumbnail = exif_dict.pop("thumbnail", None)

    if "GPS" in exif_dict:
        gps_info = exif_dict["GPS"]
        for tag in gps_info:
            tag_name = piexif.TAGS["GPS"][tag]["name"]
            print(f"{tag_name}: {gps_info[tag]}")

    if gps_info:
        latitude, longitude = get_decimal_coordinates(gps_info)
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
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

localizador()