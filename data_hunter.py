import requests
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
day_before_yesterday = today - datetime.timedelta(days=2)


class DataHunter:
    def __init__(self, api, key, stock):
        self.api = api
        self.key = key
        self.stock = stock

    def get_response(self):
        params0 = {"apikey": self.key,
                  "symbol": self.stock,
                  "interval": "1day",
                  "country": "India",
                  "date": yesterday
                  }

        params1 = {"apikey": self.key,
                  "symbol": self.stock,
                  "interval": "1day",
                  "country": "India",
                  "date": day_before_yesterday
                  }
        response0 = requests.get(url=self.api, params=params0).json()["values"][0]["close"]
        response1 = requests.get(url=self.api, params=params1).json()["values"][0]["close"]
        return [int(float(response0)), int(float(response1))]

    def prepare_data(self):
        # Calculate difference percentage of profit/loss
        response_list = self.get_response()
        diff_percentage = (response_list[0] - response_list[1]) / ((response_list[0] + response_list[1]) / 2) * 100
        if response_list[1] > response_list[0]:
            status = "🔺"
        else:
            status = "🔻"
        return {"percentage": diff_percentage, "status": status}


