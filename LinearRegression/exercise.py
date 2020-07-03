import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




customers = pd.read_csv('EcommerceCustomers')

print(customers.head())

#print(customers.describe())

#print(customers.info())


#sns.jointplot(data=customers, x='Time on Website', y='Yearly Amount Spent')

sns.jointplot(data=customers, x='Time on App', y='Time on Website')

#plt.show()

print(customers.columns)

y = customers['Yearly Amount Spent']

#print(y)

X = customers[['Avg. Session Length', 'Time on App', 'Time on Website']]

