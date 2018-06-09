from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

pandas_series = pd.Series([100,'foo',567,'ban'], index=['cat','dog','goat','horse'])
print(pandas_series)

d = {'one':pd.Series(['cat',35,78,'Hat'], index=['Cat','dog','food','goat']),
     'Two':pd.Series([25,56,324,'boo'], index=['Cat','dog','food','snake'])}
pandas_dataframe = pd.DataFrame(d)

pandas_dataframe = pandas_dataframe.fillna(method='ffill')

print("\n",pandas_dataframe)
print(pandas_series.index)
print(pandas_dataframe.index)

#locate elemnets
print(pandas_series.loc[['cat','goat']])
#element at index 2
print(pandas_series.iloc[2])

ndarray = np.array([100,'foo',567,'ban'])
ndarray_filter = ndarray == pandas_series

print(ndarray_filter)
print(type(ndarray))

housing_df = pd.read_csv("california_housing_test.csv" ,sep=",")
#print(housing_df)
#housing_df.hist(column="population", figsize=[6,4])
population =housing_df[["population","households"]]
households = housing_df[["population","median_income","total_bedrooms"]]
print(housing_df.tail())
print(population[:20])
print(households[20:40])
joined_df = pd.merge(population,households,how='inner')
print(joined_df[:20])
#population[:30].plot(kind='bar',figsize=[15,10])
#plt.title("Some Population Stuff")
#plt.xlabel("sample")
#plt.ylabel("census")
#plt.show()