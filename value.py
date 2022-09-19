'''
Created by fufufanatic
fufufinance determines which stocks might be undervalued by assessing the Big Three (pricetobook, pegratio, and dividends)
'''

import yfinance as yf

# Returns list of tickers scraped from nasdaqtrader document (comprehensive list of public companies listed on the NASDAQ)
def get_tickers():    
    tickers = []
    print('\n===== Tickers [Appending] =====\n')
    with open('nasdaqtrader.txt', 'r') as f:
        for line in f.readlines():
            ticker = line.split('|')[1]
            tickers.append(ticker)
            print(f'Adding to list of tickers: {ticker}')
    return tickers
        
# Returns list of potentially undervalued stock
def get_undervalued(tickers):
    utickers = []
    print('\n===== Tickers [Testing] =====\n')
    for ticker in tickers:
        print(f'Testing {ticker} ...')
        try:
            company = yf.Ticker(ticker)
            # Default numeric values are assigned to Big Three if they do not have values
            pricetobook = float( 99 if company.info['priceToBook'] is None else company.info['priceToBook'] )
            pegratio = float( 99 if company.info['pegRatio'] is None else company.info['pegRatio'] )
            div = float( 0 if company.info['fiveYearAvgDividendYield'] is None else company.info['fiveYearAvgDividendYield'] )
            # Stock is considered undervalued if book and earnings are ~greater than price, and dividends are provided
            if (0 < pricetobook <= 1.33) and (0 < pegratio <= 1) and (div > 0) :
                utickers.append(ticker)
                print(f'-- CHECK: {company.info["longName"]} ({ticker}) - {company.info["longBusinessSummary"]}')
        except:
            pass
    return utickers

# Shows pertinent information in determining potentially undervalued stock
def show_tickers(tickers):
    for ticker in tickers:
        company = yf.Ticker(ticker)
        name = company.info['longName']
        summary = company.info['longBusinessSummary']
        pricetobook = company.info['priceToBook']
        pegratio = company.info['pegRatio']
        div = company.info['fiveYearAvgDividendYield']
        # Simply prints said pertinent information
        print(f'{name} ({ticker})')
        print(f'{summary}')
        print(f'pricetobook: {pricetobook}')
        print(f'pegratio: {pegratio}')
        print(f'div: {div}\n')

# Runs main program to display potentially undervalued stock
def run_me():
    tickers = get_tickers()
    utickers = get_undervalued(tickers)
    print('\n===== Tickers [Undervalued] =====\n')
    show_tickers(utickers)

# Testing module
def test_me():
    tickers = ['MANU', 'NIO', 'AAPL', 'MSFT', 'TSLA', 'DASH']
    for ticker in tickers:
        company = yf.Ticker(ticker)
        print(company.info)
   
if __name__ == '__main__':
    run_me()