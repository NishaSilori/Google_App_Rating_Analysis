import inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from import_data import data
type(data)
data.head()
data.shape
data.describe()
data.boxplot()
plt.show()
data.hist()
plt.show()
data.info()
data.isnull().sum()
