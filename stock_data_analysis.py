import pandas as pd
#import yfinance as yf
from yahoofinancials import YahooFinancials

# Tutorial: https://towardsdatascience.com/a-comprehensive-guide-to-downloading-stock-prices-in-python-2cd93ff821d4
# Tutorial: https://pypi.org/project/yahoofinancials/

# Variable definition
n = 0
lst = []

#############
# User input
# https://www.marketwatch.com/tools/quotes/lookup.asp
print("How many stocks do you want to analyze?", end= " ")
n = int(input())
for i in range(n):
    print("Type in the ticker symbol of a stock and press enter:\n(database for help: https://www.marketwatch.com/tools/quotes/lookup.asp)", end=" ")
    lst.append(str(input()))

############
# Load the data for the stocks
print("wait.")

yahoo_financials = YahooFinancials(lst)

stock_quote_type_data = yahoo_financials.get_stock_quote_type_data()
key_statistics_data = yahoo_financials.get_key_statistics_data()
summary_data = yahoo_financials.get_summary_data()
stock_earnings_data = yahoo_financials.get_stock_earnings_data()
historical_price_data = yahoo_financials.get_historical_price_data(start_date='2019-01-01', end_date='2019-12-31', time_interval='weekly')
#financial_stmts = yahoo_financials.get_financial_stmts()

print("done.")

###########
#Print results

for i in range(len(lst)):
    print("Price to revenue ratio of", lst[i], ": ", key_statistics_data[lst[i]]["enterpriseToRevenue"])
    print("pegRatio of", lst[i], ": ", key_statistics_data[lst[i]]["pegRatio"])
    print("Estimate financials of", lst[i], ": ", stock_earnings_data[lst[i]]["financialsData"]["yearly"])



