import pandas as pd
from yahoofinancials import YahooFinancials



##############################################
##############################################
## using yahoofinancials
########
##############################################
yahoo_financials = YahooFinancials('DOCU')


# data = yahoo_financials.get_historical_price_data(start_date='2000-01-01', 
#                                                    end_date='2019-12-31', 
#                                                    time_interval='weekly')

# data = yahoo_financials.get_stock_quote_type_data()
data = yahoo_financials.get_key_statistics_data()
# data = yahoo_financials.get_summary_data()
# data = yahoo_financials.get_stock_earnings_data()
# data = yahoo_financials.get_financial_stmts()

docu_df = pd.DataFrame(data['DOCU']['forwardPE'])
docu_df = docu_df.drop('date', axis=1).set_index('formatted_date')
docu_df.head()




