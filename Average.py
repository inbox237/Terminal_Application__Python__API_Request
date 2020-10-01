
class Average:
    def ticker_average(self, ticker_days):
        start_period = 0
        avlist = []
        for i in range(len(ticker_days)):
            avlist.append(ticker_days.iloc[start_period,4])
            start_period = start_period +1
        average_value = (sum(avlist) / len(avlist))
        return (average_value)