import pandas as pd

data = pd.read_csv('ibovespa-stocks/b3_stocks_1994_2020.csv')


value_count = data['ticker'].value_counts()

search = data['ticker'] == 'ACE 3'

print(search)

#print(value_count)

print(data.head(n=10))