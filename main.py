# import all my modules

import sys
from prettytable import PrettyTable
import colorama
import datetime
from colorama import Fore
from yahoo_fin.stock_info import get_data
from Average import Average
from Yahoo import Yahoo
from Color import Color

colorama.init(autoreset=True)


# To skip welcome message and go to instructions and entering stock ticker
if "--help" in sys.argv:
    print("Here are the instructions for running the app:")
    print("Please follow the instructions at each input step")
    print("and at any of the inputs if you would like to exit")
    print("the program, just enter 'exit' as the input.")

elif "--ticker" in sys.argv:
    option_index = sys.argv.index("--ticker")
    ticker = sys.argv[option_index + 1]

# Welcome message
else:
    print("Welcome, this is Joel's Yahoo finance stock price checker.")
    print("Please follow the instructions at each step.")
    print("If you would like to exit the program, type 'exit'.\n")
    print("To get the latest LIVE price and an average of the last 30 days of")
    print("any Stock please enter a stock ticker.")
    print("For example, Apple Incorporated would be entered as 'AAPL'")


# MAIN CODE
def main():
    while True:
        ticker = None
        while ticker is None:
            try:
                ticker = input("\nPlease enter a valid Stock Ticker:\n")
                if ticker == "exit":
                    print("Program is now exiting, thank you...")
                    return

                yahoo_master = Yahoo()
                # Dates Defined
                start_time = datetime.datetime.now() - datetime.timedelta(30)
                end_date_notime = datetime.datetime.now().strftime("%m/%d/%Y")
                start_date_notime = start_time.strftime("%m/%d/%Y")
                
                
                ticker_days = get_data(ticker, start_date=start_date_notime, end_date=end_date_notime, index_as_date = True, interval="1d")
                    
                data_master = Get_data()    
                average_master = Average()
                
                # OUTPUT TABLE
                d = PrettyTable()
                d.field_names = ([Color.BOLD +Color.UNDERLINE + "Company" + Color.END , Color.BOLD + Color.UNDERLINE + "Current LIVE Price" +Color.END, Color.BOLD +Color.UNDERLINE + "Average Price 30 Days" +Color.END])
                d.add_row([Color.BOLD +Color.BLUE +  f"{ticker.upper()} - {yahoo_master.company_name(ticker)}"+ Color.END,Color.BOLD +Color.GREEN + "$""{:.2f}".format(yahoo_master.price(ticker))+Color.END,"$""{:.2f}".format(average_master.ticker_average(ticker_days))+Color.END])
                print(d)
                
            except:
                print(Fore.RED + Color.BOLD +"Ticker must be a valid Stock Ticker, please try again.")
                
                
main()

