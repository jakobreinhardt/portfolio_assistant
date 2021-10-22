import pandas as pd
import requests


def get_stock_tickers():
    
    '''
    This function reads user input on stocks to analyze
    
    input: none
    
    output: a list of stock ticker symbols to analyze
    '''
    
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
    
def read_portfolio():
    
    """Function to read portfolio data from csv.
    the csv should include column names in the first row
                
    Args:
        none
        
    Returns:
        dateframe of portfolio information
        
    """
    df = pd.read_csv("portfolio.csv", delimiter=';',  skiprows=0, encoding= 'unicode_escape')
    df.drop(index=df.index[-1], axis=0, inplace=True) # Letzte Zeile löschen 
    
    return(df)

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

def api_tickers(isin):
    
    """Function to use the openFIGI API to retrieve ticker symbols based on the ISIN of a stock
    
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