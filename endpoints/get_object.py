import requests

base_url = 'https://api.restful-api.dev/objects'

class GetObject:

    response = None
    response_json = None

    def check_status_code_is_200(self):

        assert self.response.status_code == 200

    def check_status_code_is_404(self):

        assert self.response.status_code == 404

    def get_object(self, id):

        self.response = requests.get(f'{base_url}/{id}')
        self.response_json = self.response.json()

    def check_response_id(self, id):

        assert self.response_json['id'] == id
