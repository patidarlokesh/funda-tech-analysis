# funda-tech-analysis
technical indicators (RSI, EMA, Supertrend, MACD, Volume) with fundamental metrics (P/E, ROE, Debt/Equity, EPS)

# This project performs both technical and fundamental analysis on Indian stocks using Python, yfinance, and pandas inside a Google Colab environment.
#  Fundamental Analysis using data from Yahoo Finance:
P/E Ratio
P/B Ratio
ROE (Return on Equity)
Debt-to-Equity Ratio
Market Cap, EPS, and more

#  Technical Analysis using TA-Lib indicators:
Simple Moving Average (SMA)
Relative Strength Index (RSI)

#   Data Source: yfinance (Yahoo Finance NSE data)
#   Fully run on Google Colab (no setup needed)

#    Importing Libraries

                    import yfinance as yf
                    import pandas as pd

                    nifty_50_tickers = [ ... ]
#   Custom RSI Function
                    
                    def compute_rsi(data, window=14):...
                    all_data = []

                  for ticker in nifty_50_tickers:
                      try:
                          stock = yf.Ticker(ticker)
                          info = stock.info
        hist['RSI'] = compute_rsi(hist)
        rsi_latest = hist['RSI'].iloc[-1] if len(hist) >= 14 else None
        ma_21 = hist["Close"].rolling(window=21).mean().iloc[-1] if len(hist) >= 21 else None
        ma_55 = hist["Close"].rolling(window=55).mean().iloc[-1] if len(hist) >= 55 else None

#    Fundamental Data Collection

              current_price = info.get("regularMarketPrice")

        data = {
            "Ticker": ticker,
            "Market Cap": info.get("marketCap"),
            ...
            "ROE (%)": info.get("returnOnEquity", 0) * 55 if info.get("returnOnEquity") else None,
            "ROCE (%)": info.get("returnOnEquity", 0) * 55 if info.get("returnOnEquity") else None,
            ...
            "MA21": round(ma_21, 2) if ma_21 else None,
            "MA55": round(ma_55, 2) if ma_55 else None,
            "RSI": round(rsi_latest, 2) if rsi_latest else None,
        }
#      Handle Errors        
        
        except Exception as e:
        print(f"Error fetching {ticker}: {e}")


#      Apply Fundamental & Technical Filters:

            df = df[df["P/E Ratio"].notnull() & (df["P/E Ratio"] > 15)]
            df = df[df['P/B Ratio'].notnull() & (df['P/B Ratio'] < 12)]
            df = df[df['ROCE (%)'].notnull() & (df['ROCE (%)'] > 10)]
            df = df[df['Enterprise Value/EBITDA'].notnull() & (df['Enterprise Value/EBITDA'] > 5)]
            df = df[(df['MA21'] > df['MA55']) & (df['RSI'] > 55)] 

#    Download Excel File (Only in Colab)      
            from google.colab import files
            files.download("Nifty50_Fundamental_Complete.xlsx")



                    
