import pprint
import os
import sys
import time
from tqdm import tqdm
import requests


'''
Ссылка на сам API:
https://akabab.github.io/superhero-api/api/
'''

BASE_URL = 'https://akabab.github.io/superhero-api/api/'


def get_all_info() -> [dict]:
    """
    Функция отправляет запрос к api супергероев по url
    https://akabab.github.io/superhero-api/api/api/all.json
    возвращает информацию о всех супергероях в формате json
    :return: response_json
    """
    route_for_get_all_info = "all.json"
    url = BASE_URL + route_for_get_all_info
    response_json = requests.get(url).json()
    return response_json


def get_id_and_full_name_in_all_info(json_response_obj: [dict]) -> dict:
    """
    Функция обрабатывает словарь поступающий от get_all_info
    Возвращает информацию по id и fullName супергероев
    :param json_response_obj:
    :return: gen_dict = {id : fullName}
    """
    gen_dict = {el['id']: el['biography']['fullName'] for el in json_response_obj}
    return gen_dict


def get_images_in_all_info(json_response_obj: dict):
    """
    Функция отправляет к api
    Возвращает информацию по id и всех фотографий супергероев
    :param json_response_obj:
    :return:
    """
    dict_id_and_images = {}
    for el in json_response_obj:
        id = el['id']
        dict_with_all_photoes = el['images']
        list_with_all_image = []
        for el_image in dict_with_all_photoes.values():
            list_with_all_image.append(el_image)
        dict_id_and_images[id] = list_with_all_image
    return dict_id_and_images

def get_appearance_in_all_info(json_response_obj2):
    dict_appearance_all_of = {}
    for el in json_response_obj2:
        id = el['id']
        dict_appearance_all = el['appearance']
        dict_appearance_all_of[id]=dict_appearance_all
    return dict_appearance_all_of

def get_powerstats_in_all_info(json_respons_obj_3):
    dict_powerstats_all = {}
    for el in json_respons_obj_3:
        id = el['id']
        speed = el['powerstats']['speed']
        dict_powerstats_all[id] = speed
    return dict_powerstats_all

all_info = get_all_info()
# get_id_and_full_name_in_all_info(all_info)
papka_id_image = get_images_in_all_info(all_info)
# get_appearance_in_all_info(all_info)
# get_powerstats_in_all_info(all_info)

"""
Задача:
Сформировать общую папку супергероями в директории проекта, дальше в этой папке сформировать папку под каждого героя,
названием папки должен быть id супергероя, в которую необходимо скачать все фото по API
"""
#

def check_and_create_directorie(path):
    if not os.path.exists(path):
        os.mkdir(path)

def create_image_file(path_for_image, img_data):
    with open(path_for_image, 'wb') as handler:
        handler.write(img_data)

def create_file_image_path(images):
    path_images = images.split('/')[-2::]
    for_parh_images = ' '.join(path_images)
    return for_parh_images

def create_image_in_id(papka_id_image):
    main_dir = 'test_papka2'
    check_and_create_directorie(main_dir)
    list_papka_id_image = list(papka_id_image.items())
    for id , images_list in tqdm(list_papka_id_image):
        path = f'{main_dir}/{id}'
        check_and_create_directorie(path)
        for images in images_list:
            img_data = requests.get(images).content
            for_parh_images = create_file_image_path(images)
            file_image_path = f'{main_dir}/{id}/{for_parh_images}'
            create_image_file(file_image_path, img_data)

create_image_in_id(papka_id_image)



#
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)
pprint.pprint(1)