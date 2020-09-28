# import all my modules
import requests
import json
import ftplib
import io
import pandas
import requests
import requests_html
import yahoo_fin.stock_info as yahoo



# main code

response = yahoo.get_live_price("aapl")

print(response)


