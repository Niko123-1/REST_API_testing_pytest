import requests

base_url = 'https://api.restful-api.dev/objects'

class CreateObject:

    response = None
    response_json = None

    def new_object(self, payload):

        self.response = requests.post(base_url, json=payload)
        self.response_json = self.response.json()

    def check_name(self, name):

        assert self.response_json['name'] == name

    def check_status_code_is_200(self):

        assert self.response.status_code == 200