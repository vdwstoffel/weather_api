import smtplib


class Email:
    def __init__(self, email):
        self.email = email

    def send_email(self, email, password, date, sunrise, sunset, temp, rain):

        if rain == 0:
            rain = "There will be no rain today"
        else:
            rain = "Today you can expect some rain"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(from_addr=email,
                                to_addrs=self.email,
                                msg="Subject:Daily Weather Update\n\n"
                                f"Daily weather update for {date}\n"
                                f"Sunrise: {sunrise}\n"
                                f"Sunset: {sunset}\n"
                                f"Average temperate: {temp}\n"
                                f"{rain}")
