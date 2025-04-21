user_header = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

kit_header = {
    "Authorization": "",   #Debe incluir el (authToken) del usuario para crear un kit de este usuario
    "Content-Type": "application/json"
}

kit_body = {
    "name": "",
    "cardId": "1"
}