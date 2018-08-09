from . import session, API_ENDPOINT, DUPLICATE

# class Boleto():
#     resource = "boletos"
#     endpoint = endpoint
#     duplicate = duplicate

#     def __init__(self,):
#         self.s = self.session()

#     def session(self,):
#         return requests.Session()

#     def create(self, data):
#         print(self.endpoint)
#         # return self.s.post(self.endpoint / self.resource, data=data, auth=(self.user, self.token))
#         return self.s.post(self.endpoint / self.resource, data=data)

#     def get(self, token):
#         # return self.s.get(self.endpoint / self.resource / token, auth=(self.user, self.token))
#         return self.s.get(self.endpoint / self.resource / token)

#     def duplicate_url(self, token):
#         return self.duplicate / token


class Boleto():
    RESOURCE = "boletos"

    def __init__(self, token):
        self.token = token

    def get(self):
        return session.get(API_ENDPOINT / self.RESOURCE / self.token)

    def duplicate_url(self):
        return DUPLICATE / self.token
