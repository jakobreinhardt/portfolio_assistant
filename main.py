from yahoofinancials import YahooFinancials
from functions import get_stock_tickers

print('Do you want to start an individual query [1] or do you want to check the usual suspects [2] ?' )
n = int(input())
if n == 1:
    lst = get_stock_tickers()
elif n == 2:
    lst = ['TSLA', 'TEAM', 'MSFT']
else:
    print('What do you want to do?')
    
# Load the data for the stocks
print("please wait... :-)")

yahoo_financials = YahooFinancials(lst)

stock_quote_type_data = yahoo_financials.get_stock_quote_type_data() #qualitative data of the company (e.g. Name)
summary_data = yahoo_financials.get_summary_data() #quantitative data concerned with the trading stock
key_statistics_data = yahoo_financials.get_key_statistics_data()
stock_earnings_data = yahoo_financials.get_stock_earnings_data()
historical_price_data = yahoo_financials.get_historical_price_data(start_date='2019-01-01', end_date='2019-12-31', time_interval='weekly')
financial_stmts = yahoo_financials.get_financial_stmts('annual', 'income')

print("loading completed.")

#Print results
for i in range(len(lst)):
    print('\n')

    try: print("Price to earnings(EBITDA) ratio of", stock_quote_type_data[lst[i]]['longName'], ": ", key_statistics_data[lst[i]]["enterpriseToEbitda"])
    except: print('Could not load all relevant data')

    try: print("Price to revenue ratio of", stock_quote_type_data[lst[i]]['longName'], ": ", key_statistics_data[lst[i]]["enterpriseToRevenue"])
    except: print('Could not load all relevant data')

    
    try: print("pegRatio of", stock_quote_type_data[lst[i]]['longName'], ": ", key_statistics_data[lst[i]]["pegRatio"])
    except: print('Could not load all relevant data')
    
    try: print("Estimate financials of", stock_quote_type_data[lst[i]]['longName'], ": ", stock_earnings_data[lst[i]]["financialsData"]["yearly"])
    except: print('Could not load all relevant data')


