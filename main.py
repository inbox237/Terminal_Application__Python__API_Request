import requests
import json
import ftplib
import io
import pandas
import requests
import requests_html


from yahoo_fin.stock_info import *

response = get_live_price("wbc")

print(response)


