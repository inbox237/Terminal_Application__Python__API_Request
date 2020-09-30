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