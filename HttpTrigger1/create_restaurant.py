from .db import restaurantsDb
import random


def create_restaurant_id():
    restaurant_id = random.randrange(10000, 99999)
    for restaurant in restaurantsDb:
        if restaurant['id'] == restaurant_id:
            create_restaurant_id()
    return restaurant_id


def create_restaurant(restaurat_id, name_of_restaurant, branding_color, speciality, main_chef_name):
    try:
        new_restaurant = {
            'id': restaurat_id,
            'restaurant_name': name_of_restaurant,
            'branding_color': branding_color,
            'speciality': speciality,
            'main_chef_name': main_chef_name}
        restaurantsDb.append(new_restaurant)
        return (f'El restaurante se ha creado de forma EXITOSA\n\n{restaurantsDb}')
    except:
        return 'Error: no se ha podido crear el restaurante de forma exitosa'
