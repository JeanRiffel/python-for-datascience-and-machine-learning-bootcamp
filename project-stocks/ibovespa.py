import pandas as pd
import matplotlib.pyplot as plt

def loadData():
    return  pd.read_csv('ibovespa-stocks/b3_stocks_1994_2020.csv')



def main():
    data = loadData()

    vvar3 = data.query('ticker=="VVAR3"')

    #print(vvar3)

    columns = pd.DataFrame(vvar3, columns=['high', 'low', 'datetime'])

    columns.plot(x='high', y='low',kind='line' )
    plt.show()

    print(columns)


if __name__ == "__main__":
    main()

