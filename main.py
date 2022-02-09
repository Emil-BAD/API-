import os
import sys
import pygame
import requests

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'
colors_pt = {'wt': 'белый', 'do': 'оранжевый', 'db': 'синий', 'bl': 'голубой', 'rd': 'красный', 'gn': 'зелёный'}


def geocode(address):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={address}&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
    else:
        raise RuntimeError(
            f"Ошибка выполнения запроса {geocoder_request}. HTTP-статус: {response.status_code}. ({response.reason})")
    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"] if features else None


def get_address_coords(address):
    toponym = geocode(address)
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_coordinates = toponym["Point"]["pos"]
    return ",".join(toponym_coordinates.split())


def get_pts(address, color):
    global flag_for_pt
    coord = get_address_coords(address)
    main_clr = None
    for i, j in colors_pt.items():
        if j == color.lower():
            main_clr = i
    string = f"{coord},pm{main_clr}s"
    pts.append(string)
    flag_for_pt = True


def get_photo(address):
    global flag_for_pt
    if flag_for_pt is False:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={get_address_coords(address)}&z=8&l=map"
    else:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={get_address_coords(address)}&l=map&pt={'~'.join(pts)}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    with open(map_file, "wb") as file:
        file.write(response.content)


flag_for_pt = False
pts = []
# Инициализируем pygame
pygame.init()
map_file = "map.png"
screen = pygame.display.set_mode((600, 450))
get_pts("Большая спортивная арена Лужники, Москва", "Белый")
get_pts("Стадион футбольного клуба 'Динамо', Москва", "голубой")
get_pts("Стадион футбольного клуба 'Спартак', Москва", "красный")
get_photo("Москва")
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
"""
Лужники - ll=37.560561 55.715375
Динамо - ll=37.562087 55.791627
Спартак - ll=37.440363 55.817923
"""
