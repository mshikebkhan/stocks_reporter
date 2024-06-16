from data_hunter import DataHunter
from alert_maker import AlertMaker
from postman import Postman

STOCK = "INFY:NSE"
COMPANY = "INFOSYS"

STOCKS_ENDPOINT = "https://api.twelvedata.com/time_series"
STOCKS_ENDPOINT_KEY =

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_ENDPOINT_KEY =

TWILIO_SID =
TWILIO_TOKEN =
TWILIO_NUMBER =
YOUR_NUMBER =

dh = DataHunter(api=STOCKS_ENDPOINT, key=STOCKS_ENDPOINT_KEY, stock=STOCK)
data = dh.prepare_data()

if data["percentage"] > 5:
    am = AlertMaker(api=NEWS_ENDPOINT, key=NEWS_ENDPOINT_KEY, data=data, company=COMPANY)
    alert = am.make_alert()

    p = Postman(alert=alert, sid=TWILIO_SID, token=TWILIO_TOKEN, twilio_num=TWILIO_NUMBER, num=YOUR_NUMBER)
    p.send_alert()






