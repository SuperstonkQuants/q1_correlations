from yfinance import Ticker
import src.pre_processing as pp
import datetime as dt


class Stock:
    def __init__(self, tk: Ticker):
        self.master = tk
        self.ticker = tk.ticker
        self.history = None

    def get_ticker_info(self):
        return self.master.info

    def get_history(self, start="2000-01-01", stop=dt.date.today() - dt.timedelta(1), interval='1d'):
        # TODO: Reduce the columns taken into the file. Restrict to used variables
        file_name = "{a}_{b}_{c}_{d}.csv".format(a=self.ticker, b=start, c=stop, d=interval)
        self.history = pp.read_csv(path=pp.TICKER_HISTORY_LOCATION + file_name, sep=";")
        if self.history is None:
            self.history = self.master.history(start=start, stop=stop, step=interval)
            pp.write_to_csv(pp.TICKER_HISTORY_LOCATION, file_name, self.history)
            self.history = pp.read_csv(path=pp.TICKER_HISTORY_LOCATION + file_name, sep=";")
            print("History file not up to date for {a} writing to file".format(a=self.ticker))
        print("Reading done: {a}".format(a=self.ticker))
        return self.history
