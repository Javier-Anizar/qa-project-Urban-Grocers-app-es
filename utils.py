import ssl
import requests
from requests.adapters import HTTPAdapter

class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.options |= ssl.OP_LEGACY_SERVER_CONNECT
        kwargs['ssl_context'] = context
        return super(SSLAdapter, self).init_poolmanager(*args, **kwargs)