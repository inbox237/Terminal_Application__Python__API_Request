# import all my modules

import sys
import colorama
import datetime
from colorama import Fore, Back
from prettytable import PrettyTable

import requests
import json
import ftplib
import io
import pandas
import requests
import requests_html
import yahoo_fin.stock_info as yahoo

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

# To skip welcome message and go to price
elif "--price" in sys.argv:
   option_index = sys.argv.index("--price")
   price = sys.argv[option_index + 1]

#Welcome message
else:
   print("""Welcome, this is Joel's Yahoo finance stock price checker.
Please follow the instructions at each input step and at any of the inputs if you would like to exit the program, just enter 'exit' as the input.
""")


# main code

response = yahoo.get_live_price("aapl")

print(response)


## search testing

stock1 = input("please enter a stock ticker")

print(yahoo.get_live_price(stock1))






#MAIN CODE
def main():
   while True:
      price = None
      while price is None:
         try:
            p1 = input ("""Please enter the """ + color.BOLD + "Price" +color.END+""" of your property including GST:
""")
            if p1 == "exit":
               print("Program is now exiting, thank you...")
               return
            price = float(p1)
         except:
            print(Fore.RED + color.BOLD +"Price must be a number!, please try again.")

      deposit = None
      while deposit is None:
         try:
            d1 = input ("""Please enter the """ + color.BOLD + "Deposit" +color.END+""" paid by the Purchaser including GST:
""")
            if d1 == "exit":
               print("Program is now exiting, thank you...")
               return
            deposit = float(d1)
         except:
            print(Fore.RED + color.BOLD +"The Deposit must be a number, please try again")

      isvalid = False
      while isvalid is False:
         try:
            settdate = input("Please enter the Settlement Date in format 'dd/mm/yy' : ")
            if settdate == "exit":
               print("Program is now exiting, thank you...")
               return
            else:
               try:
                  day,month,year = settdate.split('/')
                  settdate2 = datetime.date(int(year),int(month),int(day))
                  isvalid = True
                  if isvalid is True:
                     print ("")
                  else:
                     print(Fore.RED + color.BOLD +"The Settlement Date must be in format 'dd/mm/yy' only, please try again...")
               except ValueError:
                  print(Fore.RED + color.BOLD +"The Settlement Date must be in format 'dd/mm/yy' only, please try again...")
         except ValueError:
            print(Fore.RED + color.BOLD +"The Settlement Date must be in format 'dd/mm/yy' only, please try again...")

      balance = float(price-deposit)

      print("""Here are the details of your property sale so far:
      """)

#FIRST INITIAL TABLE
      d = PrettyTable()
      d.field_names = ["Details", "-", "Payable by Purchaser"]
      d.add_row(["Settlement Date",f"{settdate}",f""])
      d.add_row(["","",""])
      d.add_row(["Sale Price","","$""{:.2f}".format(price)])
      d.add_row(["Less Deposit","","$""{:.2f}".format(deposit)])
      d.add_row([color.BOLD +color.UNDERLINE + "Balance" +color.END,"", color.BOLD +color.UNDERLINE + "$""{:.2f}".format(balance) +color.END])
      print(d)

      print("""
Lets now complete the rest of the Settlement Figures to include Brisbane City Council Property Rates
""")

      print("""The current rates period is from 1 July 2020 to 30 June 2021.
""")

      ratesamount = None
      while ratesamount is None:
         try:
            ra1 = input ("""Now please enter the $ amount of rates that have been paid or should be paid for the current period:
""")
            if ra1 == "exit":
               print("Program is now exiting, thank you...")
               return
            ratesamount = float(ra1)
         except:
            print(Fore.RED + color.BOLD +"The Rates Amount must be a number!, please try again.")


      ratespaid = None
      while ratespaid != "y" and ratespaid != "n":
         try:
            ratespaid = input("""Have you paid the rates on the property for this period? Please only enter 'y' or 'n':
""")
            if ratespaid == "exit":
               print("Program is now exiting, thank you...")
               return
            elif ratespaid == "y" or ratespaid == "n":
               continue
            else:
               print(Fore.RED + color.BOLD +"The Rates Paid input must only be 'y' or 'n', please try again")
         except:
            print(Fore.RED + color.BOLD +"The Rates Paid input must only be 'y' or 'n', please try again")


#FUTURE Edit here for adjusting dates for other councils
      startrates = datetime.date(2020,7,1)
      endrates = datetime.date(2021,6,30)
      ratesdaystotal = endrates-startrates
      ratesdayspaid = endrates-settdate2
      ratesdaysunpaid = settdate2-startrates
      ratespaidfloat = float(ratesdayspaid.days)
      ratesdaystotalfloat = float(ratesdaystotal.days)
      ratesoverpaidrate = (ratespaidfloat / ratesdaystotalfloat)
      ratesoverpaid = (ratesoverpaidrate * ratesamount)
      totalbalance = (balance+ratesoverpaid)
      ratesunderpaidrate = (ratesdaysunpaid.days / ratesdaystotal.days)
      ratesunderpaid = (ratesunderpaidrate * ratesamount)
      totalbalanceunpaid = (balance - ratesunderpaid)


#TABLE FOR RATES PAID
      rp = PrettyTable()
      rp.field_names = ["Details", "-", "Payable by Purchaser"]
      rp.add_row(["Settlement Date",f"{settdate}",f""])
      rp.add_row(["","",""])
      rp.add_row(["Sale Price","","$""{:.2f}".format(price)])
      rp.add_row(["LESS Deposit","","$""{:.2f}".format(deposit)])
      rp.add_row([color.BOLD +color.UNDERLINE + "Subtotal" +color.END,"", color.BOLD +color.UNDERLINE + "$""{:.2f}".format(balance) +color.END])
      rp.add_row(["","",""])
      rp.add_row([color.BOLD+ "BCC Rates"+color.END,"",""])
      rp.add_row(["Total Rates Paid","$""{:.2f}".format(ratesamount),f""])
      rp.add_row(["Days Remaining in Rates Period",f"{ratesdayspaid.days} days",f""])
      rp.add_row(["PLUS Rates Overpaid","","$""{:.2f}".format(ratesoverpaid)])
      rp.add_row([color.BOLD +color.UNDERLINE +"TOTAL to be received at Settlement:"+color.END,"",color.BOLD +color.UNDERLINE +"$""{:.2f}".format(totalbalance)+color.END])
      

#TABLE FOR RATES UNPAID
      up = PrettyTable()
      up.field_names = ["Details", "-", "Payable by Purchaser"]
      up.add_row(["Settlement Date",f"{settdate}",f""])
      up.add_row(["","",""])
      up.add_row(["Sale Price","","$""{:.2f}".format(price)])
      up.add_row(["LESS Deposit","","$""{:.2f}".format(deposit)])
      up.add_row([color.BOLD +color.UNDERLINE + "Subtotal" +color.END,"", color.BOLD +color.UNDERLINE + "$""{:.2f}".format(balance) +color.END])
      up.add_row(["","",""])
      up.add_row([color.BOLD+ "BCC Rates"+color.END,"",""])
      up.add_row(["Total Rates Paid","$""{:.2f}".format(ratesamount),f""])
      up.add_row(["Days Remaining in Rates Period",f"{ratesdaysunpaid.days} days",f""])
      up.add_row(["LESS Rates Underpaid","","$""{:.2f}".format(ratesunderpaid)])
      up.add_row([color.BOLD +color.UNDERLINE +"TOTAL to be received at Settlement:"+color.END,"",color.BOLD +color.UNDERLINE +"$""{:.2f}".format(totalbalanceunpaid)+color.END])


      if ratespaid == "y":
         print ("""Great!, you have paid your rates, therefore the settlement figures will need to be adjusted to allow for an amount of your fully paid rates (from settlement date until the end of the current period) to be added to the total settlement amount. 
         The settlement figures are now as follows:
         """)
         print(rp)
         print("Program is now complete and will exit, thank you...")
         return
      else:
         print ("""Your rates are unpaid, therefore the settlement figures will need to be adjusted to allow for an amount of your unpaid rates (from the beginning of the rates period until Settlement Date) to be discounted from the total settlement amount. 
The settlement figures are now as follows:""")
         print (up)
         print("Program is now complete and will exit, thank you...")
         return


main()