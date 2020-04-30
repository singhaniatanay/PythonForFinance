import bs4 as bs
import pickle
import requests
import os
import datetime as dt
import pandas_datareader.data as web


def getNifty():
    resp = requests.get('https://en.wikipedia.org/wiki/NIFTY_50')
    soup = bs.BeautifulSoup(resp.text,'lxml')
    table = soup.find('table',{'class' :'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        tickers.append(row.findAll('td')[1].text)
        # print(tickers[-1])

    print('COUNT of Tickers downloaded :',len(tickers))

    with open("nifty50tickers.pickle","wb") as f:
        pickle.dump(tickers,f)

    return tickers

#getNifty()

def get_data_from_yahoo(reload_nifty=False):
    if reload_nifty:
        tickers = getNifty()
    else:
        with open("nifty50tickers.pickle","rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2010, 1, 1)
    end = dt.datetime.now()

    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker,'yahoo',start,end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already Have {}'.format(ticker))




get_data_from_yahoo()
