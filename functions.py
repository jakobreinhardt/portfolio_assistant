import webbrowser
import pandas as pd

def get_stock_tickers():
    
    '''
    This function reads user input on stocks to analyze
    A webbrowser is opened that helps the user search for stocks
    
    input: none
    
    output: a list of stock ticker symbols to analyze
    '''
    
    print("How many stocks do you want to analyze?", end= " ")
    n = int(input())
    lst = []
    print('I just opened the marketwatch webpage in your standard browser so you can search for the correct ticker symbols.')
    webbrowser.open('https://www.marketwatch.com/tools/quotes/lookup.asp', new=1, autoraise=False)
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
    df = pd.read_csv("Depot.csv", delimiter=';',  skiprows=0, encoding= 'unicode_escape')
    df.drop(index=df.index[-1], axis=0, inplace=True) # Letzte Zeile löschen 
    
    return(df)