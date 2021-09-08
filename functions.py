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
        print("Type in the ticker symbol of a stock and press enter:\n(database for help: https://www.marketwatch.com/tools/quotes/lookup.asp)", end=" ")
        lst.append(str(input()))
    return(lst)