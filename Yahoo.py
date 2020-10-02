import yfinance as yf
import yahoo_fin.stock_info as yahoo
from yahoo_fin.stock_info import get_data

import datetime


class Yahoo:
    def company_name(self, ticker):
        coname = yf.Ticker(ticker)
        company = coname.info['longName']
        return (company)

    def price(self, ticker):
        stock_price = yahoo.get_live_price(ticker)
        return (stock_price)

    def get_d(self, ticker):
        start_time = datetime.datetime.now() - datetime.timedelta(30)
        end_date_notime = datetime.datetime.now().strftime("%m/%d/%Y")
        start_date_notime = start_time.strftime("%m/%d/%Y")
        ticker_days = get_data(ticker, start_date=start_date_notime, end_date=end_date_notime, index_as_date=True, interval="1d")
        return (ticker_days)

    def get_stats(self, ticker):
        stats = yahoo.get_stats_valuation(ticker)
        return (stats)
