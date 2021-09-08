import webbrowser


####
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


####