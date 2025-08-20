# Proyecto Urban Grocers - Sp_7

### _Pruebas automatizadas para comprobar el campo 'name' al crear un kit de productos_

### Descripción

- Se diseñó una solicitud para crear un nuevo usuario mediante solicitud API.
- Se diseñó una solicitud para crear un kit personal para este usuario.
- Se automatizaron pruebas para el parametro "name" en el cuerpo de la solicitud.

### Contenido

data.py

sender_stand_request.py

configuration.py

create_kit_name_kit_test.py

### Proceso de las pruebas

1. Se crea un usuario nuevo.
2. Se obtiene el authToken para ese usuario y se utiliza en el encabezado de la solicitud para crear un kit nuevo.
3. Se especifica el valor para el parámetro 'name' que se pretende probar en el cuerpo de la solicitud para crear un kit nuevo.
4. Se envia la solicitud para crear un kit nuevo.
5. Se comprueba que la respuesta obtenida corresponde a la esperada para cada prueba: 201-prueba positiva o 400-prueba negativa. Y que el valor para el parámetro 'name' sea el mismo que el enviado en la solicitud.

### Documentación

La documentación de la API, la encuentras en:
- <URL_del_Servidor_de_Urban_Grocers>/docs/

Según los requerimientos, se utilizó la siguiente lista de comprobación:

| No. | Description                                                                                                | ER:                      |
|-----|------------------------------------------------------------------------------------------------------------|--------------------------|
| 1   | El número permitido de caracteres (1): kit_body = { "name": "a"}                                           | Código de respuesta: 201 |
| 2   | El número permitido de caracteres (511): kit_body = { "name":<Valor de prueba 1>}                          | Código de respuesta: 201 |
| 3   | El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }                  | Código de respuesta: 400 |
| 4   | El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":<Valor de prueba 2>} | Código de respuesta: 400 |
| 5   | Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	                                        | Código de respuesta: 201 |
| 6   | Se permiten espacios: kit_body = { "name": " A Aaa " }	                                                    | Código de respuesta: 201 |
| 7   | Se permiten números: kit_body = { "name": "123" }                                                          | Código de respuesta: 201 |
| 8   | El parámetro no se pasa en la solicitud: kit_body = { }                                                    | Código de respuesta: 400 |
| 9   | Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }                           | Código de respuesta: 400 |

Valor de prueba 1:
>"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"

Valor de prueba 2:
>"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"

### Configuración

#### Requisitos

- Variables de entorno:
  - URL_SERVICE (URL del servidor de Urban Grocers)
- Un Editor de código:
  - *Pycharm*
- Paquetes:
  - _pytest_
  - _requests_

#### Instrucciones

1. Clonar o descargar la carpeta del proyecto
2. Abrirla en un editor de código o IDE como _Pycharm_
3. Instalar paquetes _pytest_ y _requests_ desde terminal o en _python packages_
4. Actualizar la url del servidor en _URL_SERVICE_ en el archivo _configuration.py_. No olvides eliminar la última diagonal. 
5. Abrir la terminal y ubicarte en la carpeta del proyecto con el comando _cd <ruta/del/proyecto>_:
    ```sh
    cd projects/qa-project-Urban-Grocers-app-es
    ```
6. Ejecuta el comando _pytest_:
    ```sh
   pytest
    ``` 
- El comando _pytest_ ejecutará los archivos que comienzan con test_ o terminan con _test dentro de la ruta 
del proyecto especificada, no distingue entre mayúsculas y minúsculas.

> NOTE_1: Si deseas modificar los datos del usuario nuevo, el cuerpo de la solicitud _user_body_ se encuentra en el archivo _data.py_. Ejemplo: 
> {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

> NOTE_2: Si deseas modificar los datos para el kit nuevo del usuario, el cuerpo de la solicitud _kit_body_ se encuentra en el archivo _data.py_. Ejemplo:
> {
    "name": "Mi conjunto",
    "cardId": "1"
}


