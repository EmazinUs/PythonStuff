import pandas as pd

df = pd.read_csv('Numpy\panda\data.csv')
print(df.head())
print(df.to_string())
print(pd.__version__)
#print(df.corr())