from base_client import BaseClient
import requests, json

# Класс получает на вход username и возвращает ID пользователя
class IDFromUsername(BaseClient):
    BASE_URL = 'https://api.vk.com/method/users.get'
    http_method = 'GET'

    def get_params(self):
        return 'user_ids'

    def __init__(self, name):
        self.name = name

    def _get_data(self, method, http_method):
        response = requests.get(self.BASE_URL + '?' + self.get_params() + '=' + self.name)
        return self.response_handler(response)

    def response_handler(self, response):
        parsed = json.loads(response.text)
        try:
            return parsed.get('response')[0].get('uid')
        except:
            return -1

