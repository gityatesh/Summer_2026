import numpy as np
import pandas as pd
dirty_data = {
    "Symbol": ["RELIANCE", "TCS", "TCS", "INFY", "HDFCBANK", "ITC", "WIPRO"],
    "Sector": ["Energy", "Technology", "Technology", "Technology", "Banking", "Consumer", None],
    "Price": [2850.50, 3950.00, 3950.00, np.nan, 1530.80, 425.10, 300.00],
    "Volume": [4500000, 2100000, 2100000, 3200000, np.nan, 8900000, 1500000]
}

df = pd.DataFrame(dirty_data)

#drops the duplicate row
df.drop_duplicates(inplace=True)

#drops the row if some info is missing in it
df.dropna(subset=['Sector'], inplace=True)


print(df)

#check how much null values are there in our data
print('count null data: ')
print(df.isnull().sum())
print(df.duplicated().sum())

#to fill the nans with data
average = df['Price'].mean()
df['Price'] = df['Price'].fillna(average, inplace=True)
df['Volume']=df['Volume'].fillna(0, inplace=True)

