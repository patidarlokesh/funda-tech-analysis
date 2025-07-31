import yfinance as yf
import pandas as pd


nifty_50_tickers = [
    "ABB.NS", "ACC.NS", "APLAPOLLO.NS", "AUBANK.NS", "ADANIENSOL.NS", "ADANIENT.NS", "ADANIGREEN.NS", "ADANIPORTS.NS",
    "ADANIPOWER.NS", "ATGL.NS", "ABCAPITAL.NS", "ABFRL.NS", "ALKEM.NS", "AMBUJACEM.NS", "APOLLOHOSP.NS", "APOLLOTYRE.NS",
    "ASHOKLEY.NS", "ASIANPAINT.NS", "ASTRAL.NS", "AUROPHARMA.NS", "DMART.NS", "AXISBANK.NS", "BSE.NS", "BAJAJ-AUTO.NS",
    "BAJFINANCE.NS", "BAJAJFINSV.NS", "BAJAJHLDNG.NS", "BAJAJHFL.NS", "BANDHANBNK.NS", "BANKBARODA.NS", "BANKINDIA.NS",
    "MAHABANK.NS", "BDL.NS", "BEL.NS", "BHARATFORG.NS", "BHEL.NS", "BPCL.NS", "BHARTIARTL.NS", "BHARTIHEXA.NS",
    "BIOCON.NS", "BOSCHLTD.NS", "BRITANNIA.NS", "CGPOWER.NS", "CANBK.NS", "CHOLAFIN.NS", "CIPLA.NS", "COALINDIA.NS",
    "COCHINSHIP.NS", "COFORGE.NS", "COLPAL.NS", "CONCOR.NS", "CUMMINSIND.NS", "DLF.NS", "DABUR.NS", "DIVISLAB.NS",
    "DIXON.NS", "DRREDDY.NS", "EICHERMOT.NS", "ESCORTS.NS", "ETERNAL.NS", "EXIDEIND.NS", "NYKAA.NS", "FEDERALBNK.NS",
    "GAIL.NS", "GMRAIRPORT.NS", "GLENMARK.NS", "GODREJCP.NS", "GODREJPROP.NS", "GRASIM.NS", "HCLTECH.NS", "HDFCAMC.NS",
    "HDFCBANK.NS", "HDFCLIFE.NS", "HAVELLS.NS", "HEROMOTOCO.NS", "HINDALCO.NS", "HAL.NS", "HINDPETRO.NS", "HINDUNILVR.NS",
    "HINDZINC.NS", "HUDCO.NS", "HYUNDAI.NS", "ICICIBANK.NS", "ICICIGI.NS", "ICICIPRULI.NS", "IDFCFIRSTB.NS", "IRB.NS",
    "ITC.NS", "INDIANB.NS", "INDHOTEL.NS", "IOC.NS", "IRCTC.NS", "IRFC.NS", "IREDA.NS", "IGL.NS", "INDUSTOWER.NS",
    "INDUSINDBK.NS", "NAUKRI.NS", "INFY.NS", "INDIGO.NS", "JSWENERGY.NS", "JSWSTEEL.NS", "JINDALSTEL.NS", "JIOFIN.NS",
    "JUBLFOOD.NS", "KPITTECH.NS", "KALYANKJIL.NS", "KOTAKBANK.NS", "LTF.NS", "LICHSGFIN.NS", "LTIM.NS", "LT.NS",
    "LICI.NS", "LODHA.NS", "LUPIN.NS", "MRF.NS", "M&MFIN.NS", "M&M.NS", "MANKIND.NS", "MARICO.NS", "MARUTI.NS",
    "MFSL.NS", "MAXHEALTH.NS", "MAZDOCK.NS", "MOTILALOFS.NS", "MPHASIS.NS", "MUTHOOTFIN.NS", "NHPC.NS", "NMDC.NS",
    "NTPCGREEN.NS", "NTPC.NS", "NATIONALUM.NS", "NESTLEIND.NS", "OBEROIRLTY.NS", "ONGC.NS", "OIL.NS", "OLAELEC.NS",
    "PAYTM.NS", "OFSS.NS", "POLICYBZR.NS", "PIIND.NS", "PAGEIND.NS", "PATANJALI.NS", "PERSISTENT.NS", "PETRONET.NS",
    "PHOENIXLTD.NS", "PIDILITIND.NS", "POLYCAB.NS", "PFC.NS", "POWERGRID.NS", "PREMIERENE.NS", "PRESTIGE.NS", "PNB.NS",
    "RECLTD.NS", "RVNL.NS", "RELIANCE.NS", "SBICARD.NS", "SBILIFE.NS", "SJVN.NS", "SRF.NS", "MOTHERSON.NS", "SHREECEM.NS",
    "SHRIRAMFIN.NS", "SIEMENS.NS", "SOLARINDS.NS", "SONACOMS.NS", "SBIN.NS", "SAIL.NS", "SUNPHARMA.NS", "SUPREMEIND.NS",
    "SUZLON.NS", "SWIGGY.NS", "TVSMOTOR.NS", "TATACOMM.NS", "TCS.NS", "TATACONSUM.NS", "TATAELXSI.NS", "TATAMOTORS.NS",
    "TATAPOWER.NS", "TATASTEEL.NS", "TATATECH.NS", "TECHM.NS", "TITAN.NS", "TORNTPHARM.NS", "TORNTPOWER.NS", "TRENT.NS",
    "TIINDIA.NS", "UPL.NS", "ULTRACEMCO.NS", "UNIONBANK.NS", "UNITDSPR.NS", "VBL.NS", "VEDL.NS", "VMM.NS", "IDEA.NS",
    "VOLTAS.NS", "WAAREEENER.NS", "WIPRO.NS", "YESBANK.NS", "ZYDUSLIFE.NS"
]


def compute_rsi(data, window=14):
            delta = data['Close'].diff()

            gain = delta.where(delta > 0, 0)
            loss = -delta.where(delta < 0, 0)

            avg_gain = gain.rolling(window=window).mean()
            avg_loss = loss.rolling(window=window).mean()

            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))
            return rsi

all_data = []

for ticker in nifty_50_tickers:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # Get historical data for MA calculation
        hist = stock.history(period="130d")  # Enough to calculate MA100

        
        
        # Calculate RSI (14-period)
        hist['RSI'] = compute_rsi(hist)
        rsi_latest = hist['RSI'].iloc[-1] if len(hist) >= 14 else None


        ma_21 = hist["Close"].rolling(window=21).mean().iloc[-1] if len(hist) >= 21 else None
        ma_55 = hist["Close"].rolling(window=55).mean().iloc[-1] if len(hist) >= 55 else None
        

        current_price = info.get("regularMarketPrice")


        data = {
            "Ticker": ticker,
            "Market Cap": info.get("marketCap"),
            "P/E Ratio": info.get("trailingPE"),
            "P/B Ratio": info.get("priceToBook"),
            "EPS (TTM)": info.get("trailingEps"),
            "ROE (%)": info.get("returnOnEquity", 0) * 55 if info.get("returnOnEquity") else None,
            "ROCE (%)": info.get("returnOnEquity", 0) * 55 if info.get("returnOnEquity") else None,  # Approx
            "Debt/Equity": info.get("debtToEquity"),
            "Total Debt": info.get("totalDebt"),
            "Cash": info.get("totalCash"),
            "Enterprise Value/EBITDA": info.get("enterpriseToEbitda"),
            "Price to Cash Flow": info.get("priceToCashflow"),
            "Profit Margin (%)": info.get("profitMargins", 0) * 55 if info.get("profitMargins") else None,
            "Dividend Yield (%)": info.get("dividendYield", 0) * 55 if info.get("dividendYield") else 0,
            "Interest Coverage Ratio": info.get("ebitda") / info.get("interestExpense") if info.get("ebitda") and info.get("interestExpense") else None,
            "Free Cash Flow": info.get("freeCashflow"),
            "CFO/PAT": None,  # Not available from yfinance
            "EPS Growth (Quarterly)": info.get("earningsQuarterlyGrowth"),
            "Sales Growth (YoY)": info.get("revenueGrowth", 0) * 55 if info.get("revenueGrowth") else None,
            "Promoter Holding": None,  # Not available on yfinance
            "FII Holding": None,
            "DII Holding": None,
            "Retail Holding": None,
            "MA21": round(ma_21, 2) if ma_21 else None,
            "MA55": round(ma_55, 2) if ma_55 else None,
            "RSI": round(rsi_latest, 2) if rsi_latest else None,
            
        }

        all_data.append(data)

    except Exception as e:
        print(f"Error fetching {ticker}: {e}")

# Function to format values in Indian numbering system
def convert_to_indian_units(value):
    if value is None:
        return None
    crore = 10_000_000
    lakh = 100_000
    try:
        value = float(value)
    except:
        return value  # skip if can't convert
    if value >= crore:
        return f"{round(value / crore, 2)} Cr"
    elif value >= lakh:
        return f"{round(value / lakh, 2)} Lakh"
    else:
        return f"{round(value, 2)}"


# Convert to DataFrame
df = pd.DataFrame(all_data)

df = df[df["P/E Ratio"].notnull() & (df["P/E Ratio"] > 15)]
df = df[df['P/B Ratio'].notnull() & (df['P/B Ratio'] < 12)]
df= df[df['ROCE (%)'].notnull() & (df['ROCE (%)'] > 10)]
df = df[df['Enterprise Value/EBITDA'].notnull() & (df['Enterprise Value/EBITDA'] > 5)]
df = df[(df['MA21'] > df['MA55']) & (df['RSI'] > 55)] 

# df = df[df['RSI'].notnull() & (df['RSI'] > 55)]
# df = df[df['MA21']>df['MA55']]
# df = df[df['Free Cash Flow'].notnull() & (df['Free Cash Flow'] > 0)]


cols_to_convert = ["Market Cap", "Total Debt", "Cash", "Free Cash Flow"]

for col in cols_to_convert:
    df[col] = df[col].apply(convert_to_indian_units)


# Export to Excel
df.to_excel("Nifty50_Fundamental_Complete.xlsx", index=False)
print("✅ Data exported with Indian-style units: Nifty50_Fundamental_Complete.xlsx")

from google.colab import files
files.download("Nifty50_Fundamental_Complete.xlsx")