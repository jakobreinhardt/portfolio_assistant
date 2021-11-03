from yahoofinancials import YahooFinancials
from functions import get_stock_tickers, read_portfolio, api_tickers
import sys
import webbrowser
import time
import pandas as pd
import numpy as np
import time


# Ask for user input
k = 0
print('\n')
print('Welcome to my stock data analysis program.')

while k !=3:
    print('\n')
    print('What do you want to do?')
    print('[1] Start a manual stock analysis')
    print('[2] Analyse portfolio')
    print('[3] Exit')
    k = input()
    
    if k == 1 or k =='1':
        print('\n')
        print('Do you know the Ticker symbols?')
        print('[1] Yes')
        print('[2] No: A webpage opens for help')
        print('[3] No: Query of the ticker symbol based on ISIN number')
        i = input()
        # A webbrowser is opened that helps the user search for stocks
        if i == 2 or i =='2':  
            print('A webpage was opened in your standard browser so you can search for the correct ticker symbols.')
            webbrowser.open('https://finance.yahoo.com/lookup/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAD_j2nxxz9d9KQxok4X-j1OSRysQD9LUzRUQ7Z9PCZjdf7cGhWgyLmISIaHfq2gJzeTJs1mJ1vGgRnRzom1tqmD9Rctp0kh2vaHh-NcwNTPE-rqmG29bZzqefXj4IhP1QQBF36qlzzWIG6wK_oKsx3clfThu76jmxJwPJl9CBTgu', new=1, autoraise=False)
            # https://www.nasdaq.com/market-activity/stocks/screener
            # https://www.marketwatch.com/tools/quotes/lookup.asp
            
        elif i == 3 or i == '3':
            m = 1
            while m == 1 or m == '1':
                print('\n')
                print("What is the ISIN of the stock?")
                isin = str(input())
                try:
                    print('Ticker symbol: ', api_tickers(isin))
                except:
                    print('This did not work.')
                
                print('\n')
                print('[1] Query another Ticker symbol')
                print('[2] Continue')
                m = input()
            
        stock_list = get_stock_tickers()
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
            
            try: print('Marketcap of {}: {:.2f} B$'.format(stock_quote_type_data[stock_list[i]]['longName'], summary_data[stock_list[i]]['marketCap']/1000000000))
            except: print('Could not load all relevant data')


    if k == 2 or k =='2':
        i = 0
        while i != 4 or i != '4':
            print('\n')
            print('This part of the programm runs an ETL-pipeline that reads in the current portfolio, uses an API to derive Ticker symbols for the stocks and finally loads and displays key metrics.')
            print('If your portfolio is up to date you can skip parts 1 and 2.')
            print('\n')
            print('[1] Retrieve Ticker Symbols for the complete portfolio')
            print('[2] Retrieve metrics for the complete portfolio')
            print('[3] Display metrics for the current portfolio')
            print('[4] Exit ')
            i = input()
            if i == 1 or i == '1':
                print("loading data. please wait... :-)")     
                portfolio = read_portfolio()
                portfolio["Ticker"] = ""
                
                # retrieve Ticker Symbol for each stock and append to dataframe
                for index, row in portfolio.iterrows():
                    try: 
                        ticker = api_tickers(str(row['ISIN']))
                        print(ticker)
                        portfolio.loc[index, "Ticker"] = ticker
                    except: 
                        print('Could not retrieve data')
                        portfolio.loc[index, "Ticker"] = np.nan
                    time.sleep(12)
                    
                print("Completed.\nCurrent stock portfolio:")
                print(portfolio)
                portfolio.to_csv('portfolio_with_ticker.csv')
                    
            elif i == 2 or i == '2':
                portfolio = pd.read_csv('portfolio_with_ticker.csv')
                portfolio.drop(columns = 'Unnamed: 0', inplace=True)
                
                stock_list = portfolio['Ticker'].tolist()
                
                for index, element in enumerate(stock_list):
                    try:
                        yahoo_financials = YahooFinancials(element)
                        stock_quote_type_data = yahoo_financials.get_stock_quote_type_data()
                        key_statistics_data = yahoo_financials.get_key_statistics_data()
                        summary_data = yahoo_financials.get_summary_data()
        
                        print("Price to revenue ratio of", stock_quote_type_data[element]['longName'], ": ", key_statistics_data[element]["enterpriseToRevenue"])
                        portfolio.loc[index, "Price to revenue"] = key_statistics_data[element]["enterpriseToRevenue"]
                        print('Marketcap of {}: {:.2f} B$'.format(stock_quote_type_data[element]['longName'], summary_data[element]['marketCap']/1000000000))
                        portfolio.loc[index, "Price to revenue"] = summary_data[element]['marketCap']/1000000000
                    except:
                        print('Could not retrieve data')
                        portfolio.loc[index, "Price to revenue"] = np.nan
                
                print("loading completed.\nCurrent stock portfolio:")
                print(portfolio)
                portfolio.to_csv('portfolio_with_ticker_info_'+time.strftime("%Y-%m-%d")+'.csv')
    
            elif i == 3 or i == '3':
                portfolio = pd.read_csv('portfolio_with_ticker_info.csv')
                print(portfolio.sort_values(by = ['Price to revenue'], ascending = False).to_string())
                
            elif i == 4 or i == '4':
                print('See you soon.')
                sys.exit()

    elif k == 3 or k == '3':
        print('See you soon.')
        sys.exit()


