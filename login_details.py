import json


class Login:
    def __init__(self, filename):
        self.filename = filename

    def get_credentials(self):
        try:
            with open(self.filename) as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Valid credentials file not found!")
            return False
        else:
            owm_api = data["OWM_API"]
            pixela_user = data["PIXELA_USER"]
            pixela_token = data["PIXELA_TOKEN"]
            email = data["SERVER_EMAIL"]
            email_password = data["SERVER_EMAIL_PASSWORD"]

            return owm_api, pixela_user, pixela_token, email, email_password
