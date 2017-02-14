import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import os 
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

style.use('ggplot')

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

#save_sp500_tickers()

def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2000,1,1)
    end = dt.datetime(2016,12,31)

    #grab all 500 tickers
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

#get_data_from_yahoo()

def compile_data():
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    for count,ticker in enumerate(tickers):
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns = {'Adj Close': ticker}, inplace = True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df

        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)

    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')

def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    #df['AAPL'].plot()
    #plt.show()
    df_corr = df.corr()
    print(df_corr.head)

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.show()
    

def loop_data():
    df = pd.read_csv('stock_dfs/FB.csv')
    #print(df.head())
    dates = list(df['Date'])
    open_prices = list(df['Open'])
    high_prices = list(df['High'])
    low_prices = list(df['Low'])
    close_prices = list(df['Close'])
    volumes = list(df['Volume'])
    adj_closes = list(df['Adj Close'])
    for i in range(len(dates)-1):
        '''print ('Date', dates[i])
        print ('High', high_prices[i])
        print ('Low', low_prices[i])
        print ('Close', close_prices[i])
        print ('Volume', volumes[i])
        print ('AdjClose', adj_closes[i])
        print ("")'''
        #check if there was over a 10% gain from one day to next
        if ((adj_closes[i+1] / adj_closes[i]) > 1.10):

            
            gain = adj_closes[i+1] / adj_closes[i]
            gain_decimal = gain - int(gain)
            gain_decimal = gain_decimal * 100
            
            print('Gain of', '{0:.2f}'.format(gain_decimal) + '%')
            print('Date', dates[i])
            print('')

        if (1 - (adj_closes[i+1] / adj_closes[i]) > .10):
            print('Loss of', '{0:.2f}'.format(100 * (1 - (adj_closes[i+1] / adj_closes[i]))) + '%') 
            print('Date', dates[i])
            print('')
        

loop_data()

