from datetime import datetime
import time
import requests

from requests import Session

ifttt_webhooks_url = "https://maker.ifttt.com/trigger/{}/with/key/{}"
btc_api_url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
convert_currency = 'USD'
parameters = {
    "id": 1,
    "convert": convert_currency,
    "aux": 'num_market_pairs'
}
session = Session()


def get_btc_price(btc_api_key):

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': btc_api_key,
    }
    session.headers.update(headers)
    response = session.get(btc_api_url, params=parameters)
    response_json = response.json()
    return round(float(response_json['data']['1']['quote']['USD']['price']), 2)


def post_ifttt_webhook(ifttt_webhooks_key, event, value):
    data = {'value1': value}
    ifttt_event_url = ifttt_webhooks_url.format(
        event, ifttt_webhooks_key)
    requests.post(ifttt_event_url, json=data)


# bitcoin_price_threshold = 10000


def main():
    # bitcoin_history = []
    btc_api_key = input("Enter your coinmarketcap API: ")
    ifttt_webhooks_key = input("Enter your IFTTT webhooks key: ")

    while True:
        price = get_btc_price(btc_api_key)
        date = datetime.now()
        # bitcoin_history.append({'date': date, 'price': price})

        #! emergency notification
        # if price < bitcoin_price_threshold:
        #     post_ifttt_webhook('bitcoin_price_emergency', price)

        #! regular price updates
        # if len(bitcoin_history) == 5:
        formatteddate = date.strftime('%d.%m.%Y %H:%M:%S')
        post_ifttt_webhook(ifttt_webhooks_key,
                           'bitcoin_price_update', f"{price}, {formatteddate}")
        # bitcoin_history = []
        print(f"\nBitcoin is at {price}USD, {formatteddate}.")
        print("Notification sent!")
        time.sleep(5*60)


if __name__ == '__main__':
    main()
    # globals()[sys.argv[1]](sys.argv[2])

    # 6312f03b-2241-4c51-8ddd-dc56aa191cd3 BTC_API_KEY
    # o7DaqXL0n-I-UnH6mYxPLQhqdhN74deO93Dq_Mz-ok6 IFTTT_WEBHOOKS_KEY
