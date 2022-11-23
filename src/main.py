import requests
import config

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={config.api_key}"
r = requests.get(url)
data = r.json()

print(data)