from urlpath import URL

DOMAIN = "https://boletocloud.com"
SANDBOX_DOMAIN = "https://sandbox.boletocloud.com"
API = "api"
VERSION = "v1"

endpoint = URL(SANDBOX_DOMAIN, API, VERSION)
duplicate = URL(SANDBOX_DOMAIN, "boleto/2via")
