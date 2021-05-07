import logging

import azure.functions as func
from .create_restaurant import create_restaurant_id, create_restaurant


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name_of_restaurant = req.params.get('restaurant_name')
    branding_color = req.params.get('branding_color')
    speciality = req.params.get('speciality')
    main_chef_name = req.params.get('main_chef_name')

    if not name_of_restaurant or branding_color or speciality or main_chef_name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name_of_restaurant = req.params.get('restaurant_name')
            branding_color = req.params.get('branding_color')
            speciality = req.params.get('speciality')
            main_chef_name = req.params.get('main_chef_name')

    if name_of_restaurant and branding_color and speciality and main_chef_name:
        restaurant_id = create_restaurant_id()
        response_create_restaurant = create_restaurant(
            restaurant_id, name_of_restaurant, branding_color, speciality, main_chef_name)
        return func.HttpResponse(response_create_restaurant)
    else:
        return func.HttpResponse(
            "ERROR - Alguno de los parametros necesarios esta vacio!",
            status_code=200
        )
