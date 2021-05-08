# funciones de administracion de restaurantes
Usaremos el servicio de Administracion de restaurantes, cuya funcion es gestionar la creacion, eliminacion y actualizacion de los restaurantes en la plataforma. Asi mismo se encrga de devolver a los usuarios informacion que este requiera sobre el restaurante, tales como los platos de la carta, hora de apertura y cierre, especialidad, nombre de los chefs, etc.

**Crearemos 3 funciones que funcionaran asi.**

**1.** Una funcion que se encargara de dar de alta nuevos restaurantes, para eso recibira El nombre del restaurante, color de la empresa, especialidad, nombre del chef y se le retornaran los mismo datos que usuario ingreso y un numero de 5 cifras generado aleatoriamente el cual sera el ID del restaurante dentro de la plataforma, se debe validar que el ID no se encuentre asignado a otro restaurante.

URI: https://adminrestaurants.azurewebsites.net/api/HttpTrigger1?restaurant_name= **nombre del restaurante**&branding_color=**color de la marca**&speciality=**especialidad**&main_chef_name=**nombre del chef**

Los valores que estan en negritas se deben cambiar por el valor correspondiente sin comillas. si el valor tiene espacios use %20 para representarlo.

**2.** Una funcion que se encargara de agregar platos al menu, se debe pasar el ID del restaurante, el nombre del plato, el valor en pesos colombianos, se debe especificar si es un entrante, un plato fuerte, un postre o una bebida, de la misma forma se debe validar que el ID del restaurante exista y que los parametros que se pasen sean coherente de lo contrario se debe devolver un error.

URI:https://adminrestaurants.azurewebsites.net/api/HttpTrigger2?restaurant_id= **ID del restaurante**&plate_name=**nombre del plato**&plate_price=**precio del plato**&plate_category=**categoria del plato**

ID de restaurante de prueba: **34567** y **78903**

La opciones para la categoria son: Entrada, Plato fuerte, postre o bebida

**3.** Una funcion que recibira un ID de restaurante y un tipo de info que quiera recibir, como respuesta la funcion devolvera solola info que el usuario a solicitado sobre el restaurante. La informacion que se puede solicitar es el nombre del chef en turno, la carta vigente(todos los platos con nombre, precio y categoria) y hora de cierre del dia vigente.

URI: 
