### Yahoo Classes
coname = yf.Ticker(symbol)
company = coname.info['longName']

print(company)

#Output = 'Microsoft Corporation'


###Classes GENERAL
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)


print(f"""{yahoo.get_live_price(symbol)}
""")
print(Yahoo().Price(symbol))


#FIRST INITIAL TABLE
d = PrettyTable()
d.field_names = ["Details", "-", "Payable by Purchaser"]
d.add_row(["Settlement Date","",""])
d.add_row(["","",""])
d.add_row(["Sale Price","","$""{:.2f}".format(Yahoo.company_name)])
d.add_row(["Less Deposit","","$""{:.2f}".format(Yahoo.price)])
d.add_row([color.BOLD +color.UNDERLINE + "Balance" +color.END,"", color.BOLD +color.UNDERLINE + "$""{:.2f}".format(balance) +color.END])

print(d)



ticker =  input(f"""To get the latest LIVE price of any Stock please enter a stock ticker, for example, Apple Incorporated would be entered as AAPL.

""")


"$""{:.2f}".format(yahoo_master.price(ticker))