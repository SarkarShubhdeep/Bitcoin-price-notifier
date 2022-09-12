# Bitcoin-price-notifier
A BTC price alert system which sends a notification to phone in every 5 minutes (which can be changed in main.py) using IFTTT webhooks and coinmarketcap API. 

## Setup
This app is dependent on two services - Coinmarketcap which will provide us with the bitcoin price updates, and IFTTT which will deliver us those price updates in the form of notifications. 

### Coinmaketcap API

Follow these steps now to get your api from coinmarketcap - 
1. Go to [https://coinmarketcap.com/api/](https://coinmarketcap.com/api/) and signup.
2. Once you are logged in you will be forwarded to your dashboard.
3. Click on COPY KEY and save it somewhere.

> You don’t need premium account for this. A basic will work just fine.

### IFTTT applet

An applet on IFTTT is something that will do stuff when a certain condition is matched - “if-this-then-that”. The process here is not very intricate. In the [main.py](http://main.py) an infinite while loop will run and inside this loop an IFTTT applet is triggered in every 5 mins. 

Follow these steps to create the applet - 

1. Go to [https://ifttt.com/](https://ifttt.com/)  and create an account.
2. Click on create
3. Click on “If This” and then search for “Webhooks” service (you can check [https://ifttt.com/maker_webhooks](https://ifttt.com/maker_webhooks) for more info on webhooks)
4. Click on “Receive a web request”, and set event name as “bitcoin_price_update”. 
It is important that you enter event name exactly this. But feel free to change it from in the main.py. 
5. Click the “Then That” button and search for notifications. Select “Send a rich notification from the IFTTT app”. 
    1. Download IFTTT app on phone and sign with the same account.
    2. On the newer versions of android, you might need to turn on the notifications permission manually.
6. Set the Message as - “Bitcoin price at {{Value1}}”
7. Set the Title as - “Bitcoin price update”
8. (Optional) Set Link URL as - “[https://coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/)”.
9. Click on “Create action” button and then “Continue”. Give an applet title and “Finish”.

Steps to get the IFTTT key -
1. Go the applet page and click on webhooks icon. It’s the triangle with dots at corners above the title.
2. Once you are on the “Webhooks integrations” page, click on “Documentation” button. 
3. This will get you to your IFTTT key. Copy it and save it.

> IFTTT takes about 10secs or so to send a notification.


Great!. Once you are done with these steps, you can fire up the main.py using terminal. Program will ask you for two inputs - 
```python
❯ python3 main.py
Enter your coinmarketcap API: YOUR_COINMARKETCAP_API
Enter your IFTTT webhooks key: YOUR IFTTT_WEBHOOKS_KEY
```
If everything goes well, we will start receiving notifications on the phone as well as on terminal.
```
Bitcoin is at 22347.32, 12.09.2022 20:12:59.
Notification sent!

Bitcoin is at 22326.5, 12.09.2022 20:18:02.
Notification sent!
```

