from .db import platesDb

def create_plate_id():
    i=0
    plate_id = random.randrange(100, 999)
    for restaurant in platesDb:
        if restaurant['menu'][i]['plate_id'] == restaurant_id:
            create_plate_id()
        i+=1
    return plate_id

def add_plate(restaurant_id, plate_id, plate_name, plate_price, plate_category):
    try:
        new_plate = {
            'plate_id': plate_id,
            'plate_name': plate_name,
            'price': plate_price,
            'plate_category': plate_category }
        
        for restaurant in platesDb:
            if restaurant_id == restaurant['restaurant_id']:
                restaurant['menu'].append(new_plate)
                return (f'El plato se ha añadido de forma EXITOSA al restaurante con id {restaurant_id}\n\n{restaurant}')
    except:
        return 'Error: no se ha podido añadir el plato de forma exitosa'