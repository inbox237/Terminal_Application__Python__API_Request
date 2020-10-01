import yfinance as yf
import yahoo_fin.stock_info as yahoo

class Yahoo:
    def company_name(self, ticker):
        coname = yf.Ticker(ticker)
        company = coname.info['longName']
        return (company)
        
    def price(self, ticker):
        stock_price = yahoo.get_live_price(ticker)
        return (stock_price)