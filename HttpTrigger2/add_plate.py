from .db import platesDb
import random

def create_plate_id():
    plate_id = random.randrange(100, 999)
    for restaurant in platesDb:
        for i in range (len(restaurant['menu'])):
            if restaurant['menu'][i]['plate_id'] == plate_id:
                create_plate_id()
    return plate_id

def add_plate(restaurant_id, plate_id, plate_name, plate_price, plate_category):
    try:
        new_plate = {
            'plate_id': plate_id,
            'plate_name': plate_name,
            'price': plate_price,
            'plate_category': plate_category }
        
        for plate in platesDb:
            if restaurant_id == plate['restaurant_id']:
                plate['menu'].append(new_plate)
                return (f'El plato se ha añadido de forma EXITOSA al restaurante con id {restaurant_id}\n\n{plate}')

        return 'El Id ingresado no corresponde a ningun restaurante registrado'
    except:
        return 'Error: no se ha podido añadir el plato de forma exitosa'