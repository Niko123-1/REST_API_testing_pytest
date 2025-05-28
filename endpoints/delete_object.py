import requests

base_url = 'https://api.restful-api.dev/objects'

class DeleteObject:

    response = None
    response_json = None

    def check_status_code_is_200(self):

        assert self.response.status_code == 200

    def delete_object(self, id):

        self.response = requests.delete(f'{base_url}/{id}')
        self.response_json = self.response.json()

    def check_deletion_message(self,id):

        assert self.response.json()['message'] == f'Object with id = {id} has been deleted.'