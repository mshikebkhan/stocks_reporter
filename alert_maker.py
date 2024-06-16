import requests

class AlertMaker:
    def __init__(self, api, key, data, company):
        self.api = api
        self.key = key
        self.data = data
        self.company = company

    def make_alert(self):
        params = {"apiKey": self.key,
                  "q": self.company.lower(),
                  "language": "en"}
        response = requests.get(url=self.api, params=params).json()
        alert = (f"{self.company}: {self.data['status']} {round(self.data['percentage'], 2)}\n"
                 f"Headline: {response['articles'][0]['title']}\n"
                 f"Brief: {response['articles'][0]['description']}")
        return alert