from import_data import data
import pandas as pd
def impute_median(series):
    return series.fillna(series.median())