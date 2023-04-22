import yfinance as yf  # Yahoo Finance Data Base

# Read Stock Info. From Yahoo API
# 1) stock_id: e.g. "2330.TW" (上市：TW), "8069.TWO" (上市：TWO)
#              You can look up stocks' id on Yahoo's website
# 2) start_date: in form like "2023-04-23"
# 3) end_date: if not assigned, loading in all data after start_date, inclusively
def GetHistoricalData(stock_id, 
                      start_date, 
                      end_date = None):
    import pandas as pd
    d = yf.Ticker(stock_id)  # Abstract the stock info. from YahooFinance
    df = d.history(start = start_date, end = end_date)
    df.columns = df.columns.str.lower()
    df.columns = pd.Series(df.columns).str.capitalize().values
    return df.dropna()