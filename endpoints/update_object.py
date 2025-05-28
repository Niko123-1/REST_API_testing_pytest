import requests

base_url = 'https://api.restful-api.dev/objects'

class UpdateObject:

    response = None
    response_json = None

    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    def update_object(self, id, payload):

        self.response = requests.put(f'{base_url}/{id}', json=payload)
        self.response_json = self.response.json()

    def check_name(self, name):

        assert self.response_json['name'] == name

    def check_data(self, data):

        assert self.response_json['data']['year'] == data['year']
        assert self.response_json['data']['price'] == data['price']
        assert self.response_json['data']['CPU model'] == data['CPU model']
        assert self.response_json['data']['Hard disk size'] == data['Hard disk size']