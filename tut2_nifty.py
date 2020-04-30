import bs4 as bs
import pickle
import requests

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

#getNifty()

def get_data_from_yahoo(reload_nifty=False):
