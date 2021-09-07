import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

########
## USING yfinance
########
################################################
#tsla_df = yf.download('TSLA')

# Tesla data from specific date
# tsla_df = yf.download('TSLA', 
#                       start='2020-01-01', 
#                       end='2020-12-10' 
#                       )
# tsla_df.head()

###############################################
# ticker = yf.Ticker('TSLA')
# tsla_df = ticker.history(period="max")
# tsla_df['Close'].plot(title="TSLA's stock price")


##############################################
##############################################
## using yahoofinancials
########
##############################################
yahoo_financials = YahooFinancials('DOCU')
#yahoo_financials = YahooFinancials('NVO') # Novo Nordisk
#yahoo_financials = YahooFinancials('TSLE') # Tesla

# data = yahoo_financials.get_historical_price_data(start_date='2000-01-01', 
#                                                    end_date='2019-12-31', 
#                                                    time_interval='weekly')

# data = yahoo_financials.get_stock_quote_type_data()
data = yahoo_financials.get_key_statistics_data()
# data = yahoo_financials.get_summary_data()
# data = yahoo_financials.get_stock_earnings_data()
# data = yahoo_financials.get_financial_stmts()

docu_df = pd.DataFrame(data['DOCU']['prices'])
docu_df = docu_df.drop('date', axis=1).set_index('formatted_date')
docu_df.head()

tsla_df = pd.DataFrame(data['TSLA']['prices'])
tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
tsla_df.head()


##############################################
# assets = ['TSLA', 'MSFT', 'FB']

# yahoo_financials = YahooFinancials(assets)

# data = yahoo_financials.get_historical_price_data(start_date='2019-01-01', 
#                                                   end_date='2019-12-31', 
#                                                   time_interval='weekly')

# prices_df = pd.DataFrame({
#     a: {x['formatted_date']: x['adjclose'] for x in data[a]['prices']} for a in assets
# })