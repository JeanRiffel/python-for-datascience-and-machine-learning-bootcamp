import pandas as pd

#df = pd.read_csv('data.csv')

#for index, row in df.iterrows():
    #print(index, row) 


data = {
    "orange" : [1,3,6],
    "apple" : [2,3,4]
}

st = ['jean', 'luiza', 'jonas']

df = pd.DataFrame(data, index=st)

#print(df.loc['luiza'])

#print(df.head())

#print(df.info())

print(df.shape)