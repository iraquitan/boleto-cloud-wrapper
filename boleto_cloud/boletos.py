import requests

from .utils import environ
from .endpoints import endpoint, duplicate


class Boleto():
    resource = "boletos"
    user = environ("BOLETO_CLOUD_USER")
    token = environ("BOLETO_CLOUD_TOKEN")
    endpoint = endpoint
    duplicate = duplicate

    def __init__(self,):
        self.s = self.session()

    def session(self,):
        return requests.Session()

    def create(self, data):
        print(self.endpoint)
        return self.s.post(self.endpoint / self.resource, data=data, auth=(self.user, self.token))

    def get(self, token):
        return self.s.get(self.endpoint / self.resource / token, auth=(self.user, self.token))

    def duplicate_url(self, token):
        return self.duplicate / token
