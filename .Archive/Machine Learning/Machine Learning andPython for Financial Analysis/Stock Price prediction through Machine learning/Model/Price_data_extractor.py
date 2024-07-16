import urllib.request
import json
from eodhd import APIClient
import pandas as pd

api = APIClient("658a1bbda0e916.80208822")
url = "https://eodhd.com/api/eod/INFY.IND?api_token=658a1bbda0e916.80208822&order=d&fmt=json"
response = urllib.request.urlopen(url)
data = pd.DataFrame(json.loads(response.read()))
print(data)