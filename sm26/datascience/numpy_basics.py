import numpy as np
np.set_printoptions(suppress = True)
# numbers = np.array([1,2,3,4,5,6,12,14,876,3265,23987.98237])
# print(numbers*8 )
# print(np.max(numbers))
import pandas as pd
rawdata = {
    "Symbol": ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ITC"],
    "Sector": ["Energy", "Technology", "Technology", "Banking", "Consumer"],
    "Price": [2850.50, 3950.00, 1640.25, 1530.80, 425.10],
    "Volume": [4500000, 2100000, 3200000, 5800000, 8900000]
}

df  = pd.DataFrame(rawdata)
print(df)
# print(df['Price'].mean())
# print(df['Sector'])
# print(df['Volume'].max())
# print(df.describe())

# print(df[['Symbol', 'Price']])

#to get our desired sector
print(df[df['Sector']=='Techonology'])