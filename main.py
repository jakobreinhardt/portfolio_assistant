#import pandas as pd
#import yfinance as yf
from yahoofinancials import YahooFinancials
from functions import get_stock_tickers



print('Do you want to start an individual query [1] or do you want to check the usual suspects [2] ?' )
n = int(input())
if n == 1:
    lst = get_stock_tickers()
elif n == 2:
    lst = ['TSLA','TEAM', 'MSFT']
else:
    print('What do you want to do?')
    
# Load the data for the stocks
print("please wait.")

yahoo_financials = YahooFinancials(lst)

stock_quote_type_data = yahoo_financials.get_stock_quote_type_data()
key_statistics_data = yahoo_financials.get_key_statistics_data()
summary_data = yahoo_financials.get_summary_data()
stock_earnings_data = yahoo_financials.get_stock_earnings_data()
historical_price_data = yahoo_financials.get_historical_price_data(start_date='2019-01-01', end_date='2019-12-31', time_interval='weekly')
#financial_stmts = yahoo_financials.get_financial_stmts()

print("loading completed.")

#Print results
for i in range(len(lst)):
    print('\n')
    print("Price to earnings(EBITDA) ratio of", lst[i], ": ", key_statistics_data[lst[i]]["enterpriseToEbitda"])
    print("Price to revenue ratio of", lst[i], ": ", key_statistics_data[lst[i]]["enterpriseToRevenue"])
    print("pegRatio of", lst[i], ": ", key_statistics_data[lst[i]]["pegRatio"])
    print("Estimate financials of", lst[i], ": ", stock_earnings_data[lst[i]]["financialsData"]["yearly"])



