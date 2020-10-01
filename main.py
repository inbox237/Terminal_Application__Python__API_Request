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
from Average import Average
from Yahoo import Yahoo
from Color import Color

colorama.init(autoreset=True)


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
                    
                    

                        
                average_master = Average()
                
                #OUTPUT TABLE
                d = PrettyTable()
                d.field_names = ([Color.BOLD +Color.UNDERLINE + "Company" + Color.END, Color.BOLD +Color.UNDERLINE + "Current LIVE Price" +Color.END, Color.BOLD +Color.UNDERLINE + "Average Price 30 Days" +Color.END])
                d.add_row([Color.BOLD +Color.BLUE +  f"{ticker.upper()} - {yahoo_master.company_name(ticker)}"+ Color.END,Color.BOLD +Color.GREEN + "$""{:.2f}".format(yahoo_master.price(ticker))+Color.END,"$""{:.2f}".format(average_master.ticker_average(ticker_days))+Color.END])
                print(d)
                
            except:
                print(Fore.RED + Color.BOLD +"Ticker must be a valid Stock Ticker, please try again.")
                
main()

