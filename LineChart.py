import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style
#from matplotlib.finance import candlestick_ohlc

def graph(ticker):

    print("!")

    df = pd.read_excel(r"C:\Users\usuario\trading-flask\venv\top_50_precios.xlsx")
    df.head()

    df = df[ticker]
    df.head()

    df.plot()
    plt.title(f"Precio de {ticker}")

    #plt.show()

    ur = r"C:/Users\usuario/trading-flask/venv/static/" 
    url = str(ur) + str(ticker) + ".png"

    print(url)

    plt.savefig(url)
    pass


if __name__ =="__main__":
    ticker = input("what ticker")
    graph(str(ticker))
