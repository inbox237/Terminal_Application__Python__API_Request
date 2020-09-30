# import all my modules

import sys
import datetime
from prettytable import PrettyTable
import requests
import json
import ftplib
import io
import pandas
import requests
import requests_html
import yahoo_fin.stock_info as yahoo
from yahoo_finance import Share
import yfinance as yf

import pdb
import colorama
import datetime
from colorama import Fore, Back

colorama.init(autoreset=True)
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   

# To skip welcome message and go to instructions and entering stock ticker
if "--help" in sys.argv:
   print("""
   Here are the instructions for running the app:
   Please follow the instructions at each input step and at any of the inputs if you would like to exit the program, just enter 'exit' as the input.
   """)

elif "--price" in sys.argv:
   option_index = sys.argv.index("--price")
   price = sys.argv[option_index + 1]

#Welcome message
else:
   print("""Welcome, this is Joel's Yahoo finance stock price checker.
Please follow the instructions at each input step and at any of the inputs if you would like to exit the program, just enter 'exit' as the input.
""")

# MAIN CODE

## MAIN INPUT

ticker =  input(f"""Please enter a stock ticker, for example, Apple Incorporated would be AAPL.

""")

## MAIN CLASSES
class Yahoo():
    def Company_Name(self, ticker):
        coname = yf.Ticker(ticker)
        company = coname.info['longName']
        return (company)
    
    def Price(self, ticker):
        stock_price = yahoo.get_live_price(ticker)
        return (stock_price)


### PRINT OUTPUTS

print("""Here are the details for stock: {company}:
      """)

#FIRST INITIAL TABLE
d = PrettyTable()
d.field_names = ["Details", "-", "Payable by Purchaser"]
d.add_row(["Settlement Date","",""])
d.add_row(["","",""])
d.add_row(["Sale Price","","$""{:.2f}".format(Yahoo.company)])
d.add_row(["Less Deposit","","$""{:.2f}".format(Yahoo.stock_price)])
d.add_row([color.BOLD +color.UNDERLINE + "Balance" +color.END,"", color.BOLD +color.UNDERLINE + "$""{:.2f}".format(balance) +color.END])

print(d)
print(Yahoo.Company_Name)
print(Yahoo.Price)