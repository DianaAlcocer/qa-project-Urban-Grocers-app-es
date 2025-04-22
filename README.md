# Proyecto Urban Grocers: 
## Pruebas para el parámetro 'name' al crear un kit

- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Ejecuta todas las pruebas con el comando pytest.
- Para la documentacion, apoyate con el recurso URL_SERVICE/docs/

Pasos a seguir para las pruebas:
1. Crear un usuario nuevo con datos válidos: Ejemplo: {"firstName": "Max","phone": "+10005553535",
      "address": "8042 Lancaster Ave.Hamburg, NY"}
2. Obtener el authToken para ese usuario.
3. Crear un kit utilizando el authToken obtenido como parte del encabezado: { "Authorization": "(authToken)" } 
y el valor de "name" de cada prueba como parte del cuerpo: {"name": "(valor de name)", "cardId": "1"}
4. Comprobar que la respuesta obtenida corresponde a la esperada para cada prueba: 201-prueba positiva o 400-prueba negativa.