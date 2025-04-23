# Diana Carolina Alcocer Garcia - Grupo 27.o - Sprint 7

# Proyecto Urban Grocers
## _Pruebas para el parámetro 'name' al crear un kit_

La documentación de la API, la encuentras en:
- <URL_SERVICE>/docs/

Necesitas tener instalados los siguientes paquetes y programas: 

| Type     | Program                   |
|----------|---------------------------|
| Terminal | Cywing                    |
| IDE      | PyCharm Community Edition |

- Puedes utilizar otras terminales como WSL, Git Bash o CMD.R
 y otros editores de código como Visual Studio Code.

| Package  | Terminal_command     |       
|----------|----------------------|       
| pytest   | pip install pytest   |       
| requests | pip install requests |

- Puedes utilizar la terminal o buscarlos en la pestaña _Python packages_ dentro de la aplicación PyCharm.

Pasos a seguir para la ejecución de las pruebas:
1. Abrir la carpeta del proyecto en un editor de código o IDE.
2. Instalar paquetes _pytest_ y _requests_.
3. Actualizar la url del servidor en _URL_SERVICE_ en el archivo _configuration.py_. No olvides eliminar la última diagonal. 
4. Abrir la terminal y ubicarte en la carpeta del proyecto con el comando _cd <ruta/del/proyecto>_. Ejemplo:
```sh
cd projects/qa-project-Urban-Grocers-app-es
```

5. Ejecuta el comando _pytest_:
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

Funcionamiento de las pruebas:
1. Se crea un usuario nuevo.
2. Se obtiene el authToken para ese usuario y se utiliza en el encabezado de la solicitud para crear un kit nuevo.
3. Se especifica el valor para el parámetro 'name' que se pretende probar en el cuerpo de la solicitud para crear un kit nuevo.
4. Se envia la solicitud para crear un kit nuevo.
5. Se comprueba que la respuesta obtenida corresponde a la esperada para cada prueba: 201-prueba positiva o 400-prueba negativa. Y que el valor para el parámetro 'name' sea el mismo que el enviado en la solicitud.
