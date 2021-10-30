import matplotlib.pyplot as plt
import pandas as pd
from data_cleaning import data
from module import impute_median
data.Rating=data["Rating"].transform(impute_median)
data.isnull().sum()
data["Type"].mode()
data["Current Ver"].mode()
data["Android Ver"].mode()
data["Type"].fillna(str(data["Type"].mode().values[0]),inplace=True)
data["Current Ver"].fillna(str(data["Current Ver"].mode().values[0]),inplace=True)
data["Android Ver"].fillna(str(data["Android Ver"].mode().values[0]),inplace=True)
data.isnull().sum()
data["Price"]=data["Price"].apply(lambda x: str(x).replace("$","") if "$" in str(x) else str(x))
data["Price"]=data["Price"].apply(lambda x: float(x))
data["Reviews"]= pd.to_numeric(data["Reviews"],errors="coerce")
data["Installs"]=data["Installs"].apply(lambda x: str(x).replace("+","") if "+" in str(x) else str(x))
data["Installs"]=data["Installs"].apply(lambda x: str(x).replace(",","") if "," in str(x) else str(x))
data["Installs"]=data["Installs"].apply(lambda x: float(x))
data.tail()
data.describe()

