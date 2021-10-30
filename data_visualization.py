from data_imputation_and_manipulation import data
import numpy as np
import matplotlib.pyplot as plt
grp= data.groupby("Category")
x=grp["Rating"].agg(np.mean)
y=grp["Price"].agg(np.sum)
z=grp["Reviews"].agg(np.mean)
x
y
z
plt.figure(figsize=(12,5))
plt.plot(x,"ro")
plt.xticks(rotation=90)
plt.title("Category wise rating")
plt.xlabel("Categories-->")
plt.ylabel("Categories-->")
plt.show()
plt.figure(figsize=(16,5))
plt.plot(y,'b--')
plt.xticks(rotation=90)
plt.title("Category wise Price")
plt.xlabel("Categories-->")
plt.ylabel("Price-->")
plt.show()
plt.figure(figsize=(16,5))
plt.plot(z,"bs")
plt.xticks(rotation=90)
plt.title("Category wise Reviews")
plt.xlabel("Categories-->")
plt.ylabel("Reviews-->")
plt.show()

