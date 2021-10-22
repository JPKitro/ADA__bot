import tweepy
import schedule
import requests

# Cripto
headers = {
    'X-CMC_PRO_API_KEY': 'db90167a-6c4c-414f-999d-524b239e97b8',
    'Accepts': 'application/json'
}

params = {
    'start': '4',
    'limit': '4',
    'convert':'USD',
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params = params, headers = headers).json()

coins = json['data']
ada_price = 0
while True:
    for coin in coins:
        if coin['symbol'] == 'ADA':
            ada_price = (str(round(coin['quote']['USD']['price'],3) ))
    break

# Twitter
consumer_key = 'EWYLexzq0jnZO4Ev6t6jfHk2a'
consumer_secret = 'VEPCXda96Zlnemz3uUdfBVkMewtv1f6OYTyzhMc3S78w4bOmWC'
key = '1451220569777741830-jlKNnB2hfXf14IzaiMbGF6pQTH5Jq5'
secret = '4FCzmpYhrFJm0V2Ir1XSUigcxrwxhMoaoMBQGS97F91H4'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def twett_price():
    api.update_status(f'Today ADA has quoted in {ada_price}USD')


def main():
    schedule.every(21600).seconds.do(twett_price)

    while True:
        try:
            schedule.run_pending()
        except tweepy.TweepError as e:
            raise e


if __name__ == "__main__":
	main()