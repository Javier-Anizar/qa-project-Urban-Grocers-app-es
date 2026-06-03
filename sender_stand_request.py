import requests
import ssl
import urllib3
from requests.adapters import HTTPAdapter
import configuration
import data

# 1. Creamos un contexto SSL personalizado que permite la renegociación
class LegacyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = ssl.create_default_context()
        ctx.options |= ssl.OP_LEGACY_SERVER_CONNECT
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        self.poolmanager = urllib3.poolmanager.PoolManager(
            ssl_context=ctx
        )

# 2. Preparamos la sesión con el adaptador
session = requests.Session()
session.mount('https://', LegacyAdapter())

# 3. Definimos las funciones usando la sesión
def post_new_user(user_body):
    return session.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=user_body,
        headers=data.headers
    )

def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return session.post(
        configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers=headers
    )