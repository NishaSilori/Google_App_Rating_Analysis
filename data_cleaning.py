from matplotlib import pyplot as plt
import pandas as pd

from import_data import data
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 20000)
pd.set_option('display.max_columns', 15)
data.isnull()
data.isnull().tail()
data.isnull().sum()
data[data.Rating>5]
data.drop([10472],inplace=True)
data[10470:10475]
data.boxplot()
plt.show()
data.hist()
plt.show()
data.isnull().sum()
threshold=len(data)*0.1
threshold
data.dropna(thresh=threshold,axis=1,inplace=True)
data.isnull().sum()
data.shape
