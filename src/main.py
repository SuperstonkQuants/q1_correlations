import src.controllers as contr
import src.pre_processing as pp
import yfinance as yf
import pandas as pd
import numpy as np
import os


def correlation_testing():
    tickers = pd.DataFrame(["GME", "AMC", "KOSS", "NAKD", "BBBY", "NOK", "VIX"], columns=['Ticker'])
    sc = contr.StockController()
    sc.init_stocks(tickers)
    for stock_name, stock in sc.stocks.items():
        stock.get_history()
    corr = {stock_name: dict() for stock_name in sc.stocks.keys()}
    norm_corr = {stock_name: dict() for stock_name in sc.stocks.keys()}
    for stock_name, stock in sc.stocks.items():
        for stock_name_2, stock_2 in sc.stocks.items():
            if stock_name == stock_name_2:
                continue
            # length = min(len(stock.history['Close']), len(stock_2.history['Close']))
            # length = 365
            length = 150
            stock_1_values = np.array(stock.history['Close'])[-length:]
            stock_2_values = np.array(stock_2.history['Close'])[-length:]
            norm_stock_1 = stock_1_values / np.sqrt(np.sum(stock_1_values**2))
            norm_stock_2 = stock_2_values / np.sqrt(np.sum(stock_2_values**2))
            corr[stock_name][stock_name_2] = float(np.corrcoef(stock_1_values, stock_2_values)[1, 0])
            norm_corr[stock_name][stock_name_2] = float(np.corrcoef(norm_stock_1, norm_stock_2)[1, 0])
    corr_df = pd.DataFrame(corr)
    norm_corr_df = pd.DataFrame(norm_corr)
    pp.write_to_csv(pp.DATA_FOLDER_LOCATION, 'corr_last_150_days.csv', corr_df)
    pp.write_to_csv(pp.DATA_FOLDER_LOCATION, 'norm_corr_last_150_days.csv', norm_corr_df)


def generate_data_folders():
    if not os.path.exists(pp.DATA_FOLDER_LOCATION):
        os.mkdir(pp.DATA_FOLDER_LOCATION)
    if not os.path.exists(pp.STOCK_FOLDER_LOCATION):
        os.mkdir(pp.STOCK_FOLDER_LOCATION)
    if not os.path.exists(pp.TICKER_HISTORY_LOCATION):
        os.mkdir(pp.TICKER_HISTORY_LOCATION)


if __name__ == "__main__":
    generate_data_folders()
    correlation_testing()
