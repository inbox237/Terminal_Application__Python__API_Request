# import all my modules

import sys
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
import argparse
import pdb
import colorama
import datetime
from colorama import Fore, Back
from yahoo_fin.stock_info import get_data

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

elif "--ticker" in sys.argv:
   option_index = sys.argv.index("--ticker")
   ticker = sys.argv[option_index + 1]

#Welcome message
else:
   print("""Welcome, this is Joel's Yahoo finance stock price checker.
   
Please follow the instructions at each input step and at any of the inputs if you would like to exit the program, just enter 'exit' as the input.
""")

# MAIN CODE
def main():
    while True:
        ticker = None
        while ticker is None:
            try:
                ticker = input ("""To get the latest LIVE price and an average of the last 30 days of any Stock please enter a stock ticker, for example, Apple Incorporated would be entered as 'AAPL'. Or to exit the app at any time, simply type 'exit'.

""")

                if ticker == "exit":
                   print("Program is now exiting, thank you...")
                   return
                check_ticker = yahoo.get_live_price(ticker)
                
                class Yahoo:
                    def company_name(self, ticker):
                        coname = yf.Ticker(ticker)
                        company = coname.info['longName']
                        return (company)
                    def price(self, ticker):
                        stock_price = yahoo.get_live_price(ticker)
                        return (stock_price)
                
                yahoo_master = Yahoo()
                
                ##Dates Defined
                start_time = datetime.datetime.now() - datetime.timedelta(30)
                start_date = start_time.strftime("%m/%d/%Y")
                end_time = datetime.datetime.today().strftime("%m/%d/%Y")
                end_date_notime = datetime.datetime.now().strftime("%m/%d/%Y")
                start_date_notime = start_time.strftime("%m/%d/%Y")
                end_pd = datetime.datetime.now().strftime("%Y-%m-%d")
                start_pd = start_time.strftime("%Y-%m-%d")
                ticker_days= get_data(ticker, start_date=start_date_notime, end_date=end_date_notime, index_as_date = True, interval="1d")
                    
                ### Average of Prices
                class Average:
                    def ticker_average(self, ticker):
                        start_period = 0
                        avlist = []
                        for i in range(len(ticker_days)):
                            avlist.append(ticker_days.iloc[start_period,4])
                            start_period = start_period +1
                        average_value = (sum(avlist) / len(avlist))
                        return (average_value)
                        
                average_master = Average()
                
                #OUTPUT TABLE
                d = PrettyTable()
                d.field_names = ([color.BOLD +color.UNDERLINE + "Company" + color.END, color.BOLD +color.UNDERLINE + "Current LIVE Price" +color.END, color.BOLD +color.UNDERLINE + "Average Price 30 Days" +color.END])
                d.add_row([color.BOLD +color.BLUE +  f"{ticker.upper()} - {yahoo_master.company_name(ticker)}"+ color.END,color.BOLD +color.GREEN + "$""{:.2f}".format(yahoo_master.price(ticker))+color.END,"$""{:.2f}".format(average_master.ticker_average(ticker))+color.END])
                print(d)
                
            except:
                print(Fore.RED + color.BOLD +"Ticker must be a valid Stock Ticker, please try again.")
                
main()

