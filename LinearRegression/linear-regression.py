import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression


df  = pd.read_csv("USA_Housing.csv")

#df.head()
#df.info()

sns.distplot(df['Price'])

##sns.heatmap(df.corr(), annot=True)

#plt.show()


x = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population', 'Price']]

y = df['Price']


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)


lm = LinearRegression()

lm.fit(X_train, y_train )

print(lm.intercept_)


cdf = pd.DataFrame(lm.coef_ , x.columns, columns=['Coeff'] )

##print(cdf)


predictions = lm.predict(X_test)

#print(predictions)

#print(y_test)
plt.scatter(y_test, predictions)
plt.show()



