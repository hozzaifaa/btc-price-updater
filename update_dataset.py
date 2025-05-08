import requests
import pandas as pd
import os
from datetime import datetime

FILE = "dataset/btc_prices.csv"
URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# Get current price
r = requests.get(URL)
price = r.json()['bitcoin']['usd']
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

# Append to CSV
df_new = pd.DataFrame([[now, price]], columns=["timestamp", "price"])

if os.path.exists(FILE):
    df = pd.read_csv(FILE)
    df = pd.concat([df, df_new], ignore_index=True)
else:
    df = df_new

df.to_csv(FILE, index=False)
