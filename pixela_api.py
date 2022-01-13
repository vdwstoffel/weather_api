import requests


class Pixela:
    def post(self, pixela_user, pixela_token, rain, temp, sun, date):

        headers = {
            "X-USER-TOKEN": pixela_token
        }

        """Post the information to Pixela"""
        # Post rain Info to Pixela #
        pix_params = {
            "date": date,
            "quantity": str(rain)
        }

        response = requests.post(url=f"https://pixe.la/v1/users/{pixela_user}/graphs/dailyrain",
                                 json=pix_params,
                                 headers=headers
                                 )
        response.raise_for_status()

        # Post temp info t0 pixela
        pix_params = {
            "date": date,
            "quantity": str(temp)
        }

        response = requests.post(url=f"https://pixe.la/v1/users/{pixela_user}/graphs/temp",
                                 json=pix_params,
                                 headers=headers
                                 )
        response.raise_for_status()

        # Post sun info to pixela
        pix_params = {
            "date": date,
            "quantity": str(sun)
        }

        response = requests.post(url=f"https://pixe.la/v1/users/{pixela_user}/graphs/sun",
                                 json=pix_params,
                                 headers=headers
                                 )
        response.raise_for_status()
