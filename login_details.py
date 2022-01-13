import json


class Login:
    def __init__(self, filename):
        self.filename = filename

    def get_credentials(self):
        with open(self.filename) as f:
            data = json.load(f)

        owm_api = data["OWM_API"]
        pixela_user = data["PIXELA_USER"]
        pixela_token = data["PIXELA_TOKEN"]

        return owm_api, pixela_user, pixela_token
