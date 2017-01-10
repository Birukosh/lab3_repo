from base_client import BaseClient
from datetime import datetime
import requests, json

class FriendsAge(BaseClient):
    BASE_URL = 'https://api.vk.com/method/friends.get'
    http_method = 'GET'


    def __init__(self, id):
        self.id = id

    def get_params(self):
        return ('user_id', 'fields')

    def get_json(self):
        pass

    def get_headers(self):
        pass



    def _get_data(self, method, http_method):
        url = self.BASE_URL + '?' + self.get_params()[0] + '=' + str(self.id) + '&' + self.get_params()[1] + '=bdate'
        response = requests.get(url)
        return self.response_handler(response)

    def response_handler(self, response):
        try:
            parsed = json.loads(response.text)
            list = parsed.get('response')
            ages = []
            for person in list:
                bdate = person.get('bdate')
                if bdate is not None:
                    try:
                        date = datetime.strptime(bdate, "%d.%m.%Y")
                        now = datetime.now()
                        ages.append(int((now - date).days / 365))
                    except ValueError:
                        continue
            return ages

        except:
            return None
