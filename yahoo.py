import platform
print('Python version = ' + platform.python_version())
import yfinance as yf
print('yfinance version = ' + yf.__version__)
import datetime

def yfinancetut(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    investment = tickerinfo['shortName']
    print('Investment: ' + investment)
    
    today = datetime.datetime.today().isoformat()
    print('Today = ' + today)
    
    tickerDF = tickerdata.history(period='id',start='2020-1-1',end=today[:10])
    priceLast = tickerDF['Close'].iloc[-1]
    priceYest = tickerDF['Close'].iloc[-2]
    change = priceLast - priceYest
    print(investment, ' price last = ', str(priceLast))
    print('Prince Change = ' + str(change) )
    print('')    
    print('************ History ************')
    print(tickerDF)
    
yfinancetut('TSLA')
print('')
yfinancetut('VOO')
