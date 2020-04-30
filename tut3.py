import bs4 as bs
import pickle
import requests
import os
import datetime as dt
import pandas_datareader.data as web
import pandas as pd

def compile_data():
    with open('nifty50tickers.pickle','rb') as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    for i,ticker in enumerate(tickers):
        df = pd.read_csv('../stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date',inplace = True)

        df.rename(columns = {'Adj Close':ticker}, inplace=True)
        df.drop(['Open','High','Low','Close','Volume'],axis=1,inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df,how='outer')

        if i % 5 == 0:
            print('We have compiled {} dfs in a single df'.format(i))

    print(main_df.head())
    main_df.to_csv('../nifty50_adj_closes.csv')




compile_data()
