import json
import requests
import csv
from pprint import pprint
import pandas as pd


url = "https://api.bitpanda.com/v1/ticker"


r = requests.get(url)
data = r.text
print(data)

df = pd.read_json(data)
df.to_csv("output1.csv")