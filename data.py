# data.py

# Encabezados para las solicitudes
headers = {
    "Content-Type": "application/json"
}

# Cuerpo para crear un usuario (necesario para obtener el token)
user_body = {
    "firstName": "Javier",
    "phone": "+12345678901",
    "address": "Calle Falsa 123"
}

# Plantilla para el kit (se modificará en las pruebas)
kit_body = {
    "name": "Mi kit"
}