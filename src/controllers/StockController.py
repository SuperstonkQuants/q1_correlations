import src.core as core
from typing import List, Set, Dict
import yfinance as yf
import pandas as pd


class StockController:
    def __init__(self):
        self.stocks = dict()  # type: Dict[str, core.Stock]
        self.current_chaining_stocks = set()  # type: Set[core.Stock]

    def init_stocks(self, df_tickers: pd.DataFrame):
        for index, row in df_tickers.iterrows():
            tmp_stock = core.Stock(yf.Ticker(row['Ticker']))
            self.stocks[tmp_stock.ticker] = tmp_stock

    def insert_stocks(self, stocks: List[core.Stock]):
        for stock in stocks:
            self.stocks[stock.ticker] = stock
