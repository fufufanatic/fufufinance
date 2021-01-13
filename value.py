'''
Created by fufufanatic
fufufinance determines which stocks might be undervalued (based on pricetobook, pegratio, dividends, and other notes from Investopedia)
'''

import yfinance as yf

def get_tickers():    
    tickers = []
    print('\n===== Tickers [Appending] =====\n')
    with open('nasdaqtrader.txt', 'r') as f:
        for line in f.readlines():
            ticker = line.split('|')[1]
            tickers.append(ticker)
            print(f'Adding to list of tickers: {ticker}')
    return tickers
        
def get_undervalued(tickers):
    # list holding potentially undervalued tickers
    utickers = []
    print('\n===== Tickers [Testing] =====\n')
    for ticker in tickers:
        print(f'Testing {ticker} ...')
        try:
            company = yf.Ticker(ticker)
            pricetobook = float( 99 if company.info['priceToBook'] is None else company.info['priceToBook'] )
            pegratio = float( 99 if company.info['pegRatio'] is None else company.info['pegRatio'] )
            div = float( 0 if company.info['fiveYearAvgDividendYield'] is None else company.info['fiveYearAvgDividendYield'] )
            if (0 < pricetobook <= 1.33) and (0 < pegratio <= 1) and (div > 0) :
                utickers.append(ticker)
                print(f'-- CHECK: {company.info["longName"]} ({ticker}) - {company.info["longBusinessSummary"]}')
        except Exception:
            pass

    return utickers

def show_tickers(tickers):
    for ticker in tickers:
        company = yf.Ticker(ticker)
        name = company.info['longName']
        summary = company.info['longBusinessSummary']
        pricetobook = company.info['priceToBook']
        pegratio = company.info['pegRatio']
        div = company.info['fiveYearAvgDividendYield']
        print(f'{name} ({ticker})')
        print(f'{summary}')
        print(f'pricetobook: {pricetobook}')
        print(f'pegratio: {pegratio}')
        print(f'div: {div}\n')

def run_me():
    tickers = get_tickers()
    utickers = get_undervalued(tickers)
    print('\n===== Tickers [Undervalued] =====\n')
    show_tickers(utickers)

def test_me():
    tickers = ['MANU', 'NIO', 'AAPL', 'MSFT', 'TSLA', 'DASH']
    show_tickers(tickers)
    #for key, value in company.info.items():
        #print(f'{key}: {value}')

def main():
    test_me()
    
if __name__ == '__main__':
    main()