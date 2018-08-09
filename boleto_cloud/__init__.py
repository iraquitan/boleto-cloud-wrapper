import requests
from urlpath import URL
from .utils import environ

USER_TOKEN = environ("BOLETO_CLOUD_USER_TOKEN")
TOKEN = environ("BOLETO_CLOUD_TOKEN", "token")
SANDBOX = environ("BOLETO_CLOUD_SANDBOX", True)


class UserTokenMissingError(Exception):
    pass

if USER_TOKEN is None:
    raise UserTokenMissingError(
        "All methods require a User API Access Token key. See "
        "https://boleto.cloud/app/dev/api#autenticacao "
        "for how to retrieve an authentication token from "
        "Boleto Cloud"
    )
session = requests.Session()
session.auth = (USER_TOKEN, TOKEN)

if SANDBOX:
    DOMAIN = "https://sandbox.boletocloud.com"
else:
    DOMAIN = "https://boletocloud.com"

API_VERSION = "v1"

API_ENDPOINT = URL(DOMAIN, "api", API_VERSION)
DUPLICATE = URL(DOMAIN, "boleto/2via")

from .boletos import Boleto
