# created by fufufanatic - comments pending

import yfinance as yf

def get_tickers():    
    tickers = []
    with open('lists/total.txt', 'r') as f:
        for line in f.readlines():
            ticker = line.split('|')[0]
            tickers.append(ticker)
    return tickers
        
def print_undervalued(tickers):
    for ticker in tickers:
        print(ticker)
        try:
            company = yf.Ticker(ticker)
            symbol = company.info['symbol']
            longname = company.info['longName']
            pricetobook = float( 99 if company.info['priceToBook'] is None else company.info['priceToBook'] )
            pegratio = float( 99 if company.info['pegRatio'] is None else company.info['pegRatio'] )
            if (0 < pricetobook <= 1) and (0 < pegratio <= 1) :
                print(symbol, longname, pricetobook, pegratio)
        except Exception:
            pass

def run_me():
    tickers = get_tickers()
    print_undervalued(tickers)

def test_me():
    company = yf.Ticker('AAPL')
    #print(company.info)
    for key, value in company.info.items():
        print(f'{key}: {value}')

def main():
    run_me()
    
if __name__ == '__main__':
    main()