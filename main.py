from functions import manual_stock_analysis, get_ticker_symbols, retrieve_metrics_full_portfolio, display_portfolio
import sys



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
        manual_stock_analysis()


    if k == 2 or k =='2':
        i = 0
        while i != 4 or i != '4':
            print('\n')
            print('This part of the programm runs an ETL-pipeline that reads in', 
                  'the current portfolio, uses an API to derive Ticker symbols for',
                  'the stocks and finally loads and displays key metrics.')
            print('If your portfolio is up to date you can skip [1] and [2].')
            print('\n')
            print('Choose to:')
            print('[1] Retrieve Ticker Symbols for the complete portfolio')
            print('[2] Retrieve metrics for the complete portfolio')
            print('[3] Display metrics for the current portfolio')
            print('[4] Go back ')
            i = input()
            if i == 1 or i == '1':
                get_ticker_symbols()
                    
            elif i == 2 or i == '2':
                retrieve_metrics_full_portfolio()
    
            elif i == 3 or i == '3':
                display_portfolio()
                
            elif i == 4 or i == '4':
                break
            
            else:
                print('\n')
                print('Wrong input. Going back to main menu:')
                break

    elif k == 3 or k == '3':
        print('See you soon.')
        sys.exit()


