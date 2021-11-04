import pandas as pd
import numpy as np
import requests
import webbrowser
from yahoofinancials import YahooFinancials
import time
import datetime


def get_ticker_symbols():
    '''   
    This function reads in the a csv file containing portfolio information
    For each row the api_tickers function is used to retrieve ticker symbols using an API
    the ticker symbols are appended to the portfolio and saved again as csv
    
    functions used: read_portfolio, api_tickers
    
    input: none
    
    output: none
    '''      
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
    
def read_portfolio():
    
    """
    Function to read portfolio data from csv.
    the csv should include column names in the first row
                
    Args:
        none
        
    Returns:
        dateframe of portfolio information
        
    """
    df = pd.read_csv("portfolio.csv", delimiter=';',  skiprows=0, encoding= 'unicode_escape')
    df.drop(index=df.index[-1], axis=0, inplace=True) # Letzte Zeile löschen 
    
    return(df)

def api_tickers(isin):
    """
    Function to use the openFIGI API to retrieve ticker symbols based on the ISIN of a stock
    
    Args:
        string containing the ISIN
        
    Returns:
        ticker symbol at US Exchange    
    """
     
    url = 'https://api.openfigi.com/v3/mapping'
    headers = {'Content-Type':'text/json'}
    data = '[{"idType":"ID_ISIN","exchCode":"US","idValue":%s}]' % '"{}"'.format(isin)
    
    r = requests.post(url, headers=headers, data=data)
    #output = r.json()
    df = pd.DataFrame(r.json()[0])

    return(df.iloc[0,0]['ticker'])
    
def retrieve_metrics():
    '''    
    reads the portfolio with Ticker information
    Uses the Yahoofinancials package to get stock data based on ticker information
    The results are saved as csv
    
    input: none
    
    output: none
    '''    
    portfolio = pd.read_csv('portfolio_with_ticker.csv')
    portfolio.drop(columns = 'Unnamed: 0', inplace=True)
    
    stock_list = portfolio['Ticker'].tolist()
    
    for index, element in enumerate(stock_list):
        try:
            yahoo_financials = YahooFinancials(element)
            stock_quote_type_data = yahoo_financials.get_stock_quote_type_data()
            key_statistics_data = yahoo_financials.get_key_statistics_data()
            summary_data = yahoo_financials.get_summary_data()

            print("Price to revenue ratio of", stock_quote_type_data[element]['longName'],
                  ": ", key_statistics_data[element]["enterpriseToRevenue"])
            portfolio.loc[index, "Price to revenue"] = key_statistics_data[element]["enterpriseToRevenue"]
            print('Marketcap of {}: {:.2f} B$'.format(stock_quote_type_data[element]['longName'], 
                                                      summary_data[element]['marketCap']/1000000000))
            portfolio.loc[index, "Marketcap"] = summary_data[element]['marketCap']/1000000000
        except:
            print('Could not retrieve data')
            portfolio.loc[index, "Price to revenue"] = np.nan
            portfolio.loc[index, "Marketcap"] = np.nan
    
    print("loading completed.\nCurrent stock portfolio:")
    print(portfolio)
    portfolio.to_csv('portfolio_with_ticker_info_'+str(datetime.date.today())+'.csv')
    
def display_portfolio():
    '''    
    prints the latest portfolio with additional information and metrics
    
    input: none
    
    output: none
    '''        
    date = datetime.date.today()
    end_date = datetime.date(2021, 11, 1)
    delta = datetime.timedelta(days=1)
    while date >= end_date:
        try: 
            portfolio = pd.read_csv('portfolio_with_ticker_info_'+str(date)+'.csv')
            break
        except: pass
        date -= delta

    print(portfolio.sort_values(by = ['Price to revenue'], ascending = False).to_string())
    
def etl_pipeline():
    '''
    ETL pipeline consisting of 3 steps 
    Extract: extracts
    Transform: 
    Load:
    
    input: none
    
    output: none
    '''    

def manual_stock_analysis():
    '''
    This function allows a manual stock analysis of one or multiple stocks. 
    Based on the user input of an ISIN number it prints the results
    
    input: none
    
    output: none
    '''
    print('\n')
    print('Do you know the Ticker symbols?')
    print('[1] Yes')
    print('[2] No: A webpage opens for help')
    print('[3] No: Query of the ticker symbol based on ISIN number')
    i = input()
    # A webbrowser is opened that helps the user search for stocks
    if i == 2 or i =='2':  
        print('A webpage was opened in your standard browser so you can search for the correct ticker symbols.')
        webbrowser.open('https://www.marketwatch.com/tools/quotes/lookup.asp', new=1, autoraise=False)
        # https://www.nasdaq.com/market-activity/stocks/screener
        
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
    
        try: print("Price to earnings(EBITDA) ratio of", stock_quote_type_data[stock_list[i]]['longName'], 
                   ": ", key_statistics_data[stock_list[i]]["enterpriseToEbitda"])
        except: print('Could not load all relevant data')
    
        try: print("Price to revenue ratio of", stock_quote_type_data[stock_list[i]]['longName'], 
                   ": ", key_statistics_data[stock_list[i]]["enterpriseToRevenue"])
        except: print('Could not load all relevant data')
        
        try: print('Marketcap of {}: {:.2f} B$'.format(stock_quote_type_data[stock_list[i]]['longName'], 
                                                       summary_data[stock_list[i]]['marketCap']/1000000000))
        except: print('Could not load all relevant data')
        

def get_stock_tickers():
    
    '''
    This function reads user input on the amount and ISIN numbers of stocks to analyze
    
    input: none
    
    output: a list of stock ticker symbols to analyze
    '''
    print('\n')
    print("How many stocks do you want to analyze?", end= " ")
    n = int(input())
    lst = []
    for i in range(n):
        print("Type in the ticker symbol of a stock (e.g. TSLA for Tesla, MSFT for Microsoft) and press enter:", end=" ")
        lst.append(str(input()))
    return(lst)


def read_data_file(file_name):
    
    """Function to read in data from a txt file. The txt file should have
    one number (float) per line. The numbers are stored in the data attribute.
                
    Args:
    file_name (string): name of a file to read from
        
    Returns:
        None
        
    """
            
    with open(file_name) as file:
        data_list = []
        line = file.readline()
        while line:
            data_list.append(int(line))
            line = file.readline()
    file.close()
    

def read_tickers():
    
    """Function to read in files containing common ticker symbols
    
    Args:
        none
        
    Returns:
        dataframe of ticker symbol information
    
    """
    df = pd.read_excel("Yahoo Ticker Symbols - September 2017.xlsx", sheet_name="Stock", skiprows=3)
    df.drop(columns=["Unnamed: 5", "Unnamed: 6", "Unnamed: 7"], inplace=True)
    
    df2 = pd.read_csv("nasdaq_screener_1634893842862.csv")
    
    return(df, df2)
