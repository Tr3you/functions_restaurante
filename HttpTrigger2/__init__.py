import logging

import azure.functions as func
from .add_plate import create_plate_id, add_plate


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    restaurant_id = req.params.get('restaurant_id')
    plate_name=req.params.get('plate_name')
    plate_price=req.params.get('plate_price')
    plate_category=req.params.get('plate_category')
    if not restaurant_id or plate_name or plate_price or plate_category:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            restaurant_id = req.params.get('restaurant_id')
            plate_name=req.params.get('plate_name')
            plate_price=req.params.get('plate_price')
            plate_category=req.params.get('plate_category')

    if restaurant_id and plate_name and plate_price and plate_category:
        plate_id = create_plate_id()
        response_add_plate = add_plate(int(restaurant_id), plate_id, plate_name, plate_price, plate_category)
        return func.HttpResponse(response_add_plate)
    else:
        return func.HttpResponse(
             "ERROR - Alguno de los parametros necesarios esta vacio!",
             status_code=200
        )
