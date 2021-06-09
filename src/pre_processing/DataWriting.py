from src.pre_processing.DataConstants import *
import pandas as pd
import os


def write_to_csv(dir_path, file_name, df: pd.DataFrame, sep=';'):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    if not os.path.exists(dir_path + file_name):
        df.to_csv(path_or_buf=dir_path + file_name, sep=sep)
        return True
    return False


def write_to_excel(dir_path, file_name, df: pd.DataFrame):
    """
    Sounds good doesn't work. For some reason it generates 0kb files, I swear I fixed it in another project.
    Now to find out which project that was...
    :param dir_path:
    :param file_name:
    :param df:
    :return:
    """
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    if not os.path.exists(dir_path + file_name):
        ew = pd.ExcelWriter(path=dir_path + file_name)
        df.to_excel(excel_writer=ew, engine='openpyxl')
        ew.save()
        ew.close()
        return True
    return False
