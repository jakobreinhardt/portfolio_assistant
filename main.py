from yahoofinancials import YahooFinancials
from functions import get_stock_tickers, read_portfolio, read_tickers
import sys
import webbrowser

# read portfolio
portfolio = read_portfolio()

# read ticker symbol list
tickers = read_tickers()

# Ask for user input
k = 0
print('Welcome to my stock data analysis program.')
while k !=2:
    print('\n')
    print('What do you want to do?')
    print('[1] Start an analysis')
    print('[2] Exit')
    k = input()
    if k == 1 or k =='1':
        print('Do you know the Ticker symbols?')
        print('[1] Yes')
        print('[2] No (A webpage will be opened to help you)')
        i = input()
        # open webpage only if help on Ticker symbols is needed
        # A webbrowser is opened that helps the user search for stocks
        if i == 2 or i =='2':  
            print('I just opened the marketwatch webpage in your standard browser so you can search for the correct ticker symbols.')
            webbrowser.open('https://www.marketwatch.com/tools/quotes/lookup.asp', new=1, autoraise=False)
        
        
        stock_list = get_stock_tickers()

        # Load the data for the stocks
        print("loading data. please wait... :-)")     
        yahoo_financials = YahooFinancials(stock_list)
        
        stock_quote_type_data = yahoo_financials.get_stock_quote_type_data() #qualitative data of the company (e.g. Name)
        summary_data = yahoo_financials.get_summary_data() #quantitative data concerned with the trading stock
        key_statistics_data = yahoo_financials.get_key_statistics_data()
        #stock_earnings_data = yahoo_financials.get_stock_earnings_data()
        #historical_price_data = yahoo_financials.get_historical_price_data(start_date='2019-01-01', end_date='2019-12-31', time_interval='weekly')
        #financial_stmts = yahoo_financials.get_financial_stmts('annual', 'income')
        print("loading completed.")
        
        
        #Print results
        for i in range(len(stock_list)):
            print('\n')
        
            try: print("Price to earnings(EBITDA) ratio of", stock_quote_type_data[stock_list[i]]['longName'], ": ", key_statistics_data[stock_list[i]]["enterpriseToEbitda"])
            except: print('Could not load all relevant data')
        
            try: print("Price to revenue ratio of", stock_quote_type_data[stock_list[i]]['longName'], ": ", key_statistics_data[stock_list[i]]["enterpriseToRevenue"])
            except: print('Could not load all relevant data')
        
            try: print("Price-Earnings-Growth (PEG) Ratio of", stock_quote_type_data[stock_list[i]]['longName'], ": ", key_statistics_data[stock_list[i]]["pegRatio"])
            except: print('Could not load all relevant data')
            
            try: print('Marketcap of {}: {:.2f} B$'.format(stock_quote_type_data[stock_list[i]]['longName'], summary_data[stock_list[i]]['marketCap']/1000000000))
            except: print('Could not load all relevant data')


    elif k == 2 or k == '2':
        print('See you soon.')
        sys.exit()
    else:
        print('\n')
        print('Invalid. Please type in [1] or [2].')
    


