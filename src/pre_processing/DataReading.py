from src.pre_processing.DataConstants import *
import pandas as pd
import os


def read_csv(path, sep) -> pd.DataFrame:
    if not os.path.exists(path):
        return None
    else:
        return pd.read_csv(path, sep=sep)


def get_nyse_tickers() -> pd.DataFrame:
    if os.path.exists(STOCK_FOLDER_LOCATION + "NYSE_Tickers.csv"):
        ticker_frame = pd.read_csv(STOCK_FOLDER_LOCATION + "NYSE_Tickers.csv", index_col=0, sep=",")
    else:
        print("This file doesn't exist. Previous generation methods are no longer maintained.")
        return
    return ticker_frame
