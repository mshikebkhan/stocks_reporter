from twilio.rest import Client


class Postman(Client):
    def __init__(self, alert, sid, token, twilio_num, num):
        super().__init__(sid, token)  # Initialize the Client with sid and token
        self.alert = alert
        self.twilio_num = twilio_num
        self.num = num

    def send_alert(self):
        self.messages.create(
            body = self.alert,
            from_ = self.twilio_num,
            to = self.num
        )
