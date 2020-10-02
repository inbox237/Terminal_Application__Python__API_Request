# import all my modules

import sys
from prettytable import PrettyTable
import colorama
from colorama import Fore
from Average import Average
from Yahoo import Yahoo
from Color import Color as Col
from http.client import InvalidURL

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

                y_mast = Yahoo()
                av_mast = Average()
                # OUTPUT TABLE 1 - Company Ticker, Company Long Name, Price and Average Price from last 30 days
                d = PrettyTable()
                d.field_names = ([
                    Col.BOLD + Col.UL + "Company" +
                    Col.END, Col.BOLD + Col.UL +
                    "Current LIVE Price" +
                    Col.END, Col.BOLD + Col.UL +
                    "Average Price 30 Days" +
                    Col.END])
                d.add_row([
                    Col.BOLD + Col.BLUE +
                    f"{ticker.upper()} - {y_mast.company_name(ticker)}" +
                    Col.END, Col.BOLD +
                    Col.GREEN +
                    "$""{:.2f}".format(y_mast.price(ticker)) +
                    Col.END, "$""{:.2f}".format(av_mast.ticker_average(y_mast.t_data(ticker))) +
                    Col.END])
                print(d)

                # OUTPUT TABLE 2 - Provides detailed valuation statistics
                e = PrettyTable()
                e.field_names = ([
                    Col.BOLD +
                    Col.UL +
                    f"Company - {ticker.upper()} - {y_mast.company_name(ticker)}" +
                    Col.END
                ])
                e.add_row([f"{y_mast.get_stats(ticker)}"])
                print(e)

            except ValueError:
                print(Fore.RED + Col.BOLD + "Not valid, please try again.")
            except IndexError:
                print(Fore.RED + Col.BOLD + "Not valid, please try again.")
            except NameError:
                print(Fore.RED + Col.BOLD + "Not valid, please try again.")
            except InvalidURL:
                print(Fore.RED + Col.BOLD + "Not valid, please try again.")


main()
