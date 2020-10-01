from main import yahoo_master.company_name as company_name
from main import yahoo_master.price as price
from main import average_master.ticker_average as ticker_average


company_name_result = company_name("AAPL")
if company_name_result != "Apple inc.":
    raise Exception("Company Name did not bring back Apple Inc. when given 'AAPL' as input!")
print("did i run")