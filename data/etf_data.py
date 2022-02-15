import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import os
from data.MCForecastTools import MCSimulation
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

# Load env
load_dotenv()
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

def get_benchmark_data(alpaca):
    tickers = ["QQQ","SPY", "IEF", "DIA"]
    today = pd.Timestamp(date.today(), tz="America/New_York").isoformat()
    three_yrs_ago=pd.Timestamp(datetime.now() - relativedelta(years=3),tz="America/New_York").isoformat()
    timeframe = "1D"
    limit_rows=1000
    prices_df_benchmark = alpaca.get_barset(
      tickers,
      timeframe,
      start=three_yrs_ago,
      end=today,
      limit=limit_rows
    ).df

    return prices_df_benchmark

def get_client_portfolio_data(alpaca, tickers):
    today = pd.Timestamp(date.today(), tz="America/New_York").isoformat()
    three_yrs_ago=pd.Timestamp(datetime.now() - relativedelta(years=3),tz="America/New_York").isoformat()
    timeframe = "1D"
    limit_rows=1000
    prices_df_client_portfolio = alpaca.get_barset(
      tickers,
      timeframe,
      start=three_yrs_ago,
      end=today,
      limit=limit_rows
    ).df

    #  Create an empty `closing_prices_df` DataFrame using Pandas
    closing_prices_client_portfolio_df = pd.DataFrame()
    # Populate the `closing_prices_df` DataFrame by accessing the `close` column from the `prices_df` DataFrame for both KO and TSLA .
    for ticker in tickers:
      closing_prices_client_portfolio_df[ticker] = prices_df_client_portfolio[ticker]["close"]
    
    daily_returns_client_portfolio_df = closing_prices_client_portfolio_df.pct_change().dropna()
    cumulative_returns_client_portfolio_df = (1+daily_returns_client_portfolio_df).cumprod()-1
    return prices_df_client_portfolio, daily_returns_client_portfolio_df, cumulative_returns_client_portfolio_df, closing_prices_client_portfolio_df 

def get_tickers(port_profile):
    tickers = []

    if port_profile == "Fixed Income":
        tickers = ["AGG", "VCIT", "HYG", "BNDX"]
    elif port_profile == "Profile 1":
        tickers = ["AGG", "VCIT", "HYG", "BNDX", "SPGP", "VXUS"]
    elif port_profile == "Profile 2":
        tickers = ["AGG", "VCIT", "HYG", "BNDX", "EMB", "SPGP", "IJH", "VXUS"]
    elif port_profile == "Profile 3":
        tickers = ["AGG", "VCIT", "HYG", "BNDX", "EMB", "SPGP", "IJH", "VB", "VXUS", "VWO"]
    elif port_profile == "Profile 4":
        tickers = ["AGG", "VCIT", "HYG", "BNDX", "EMB", "SPGP", "IJH", "VB", "VXUS", "VWO"]
    elif port_profile == "Profile 5":
        tickers = ["SPGP", "IJH", "VB", "VXUS", "VWO"]
    return tickers

def get_client_data(alpaca, tickers, client_portfolio):
    tickers = tickers
    today = pd.Timestamp(date.today(), tz="America/New_York").isoformat()
    three_yrs_ago=pd.Timestamp(datetime.now() - relativedelta(years=3),tz="America/New_York").isoformat()
    timeframe = "1D"
    limit_rows=1000
    prices_df_client = alpaca.get_barset(
      tickers,
      timeframe,
      start=three_yrs_ago,
      end=today,
      limit=limit_rows
    ).df

    #  Create an empty `closing_prices_df` DataFrame using Pandas
    closing_prices_client_portfolio_df = pd.DataFrame()
    # Populate the `closing_prices_df` DataFrame by accessing the `close` column from the `prices_df` DataFrame for both KO and TSLA .
    for ticker in tickers:
      closing_prices_client_portfolio_df[ticker] = prices_df_client[ticker]["close"]
    
    daily_returns_client=closing_prices_client_portfolio_df.pct_change().dropna()
    cumulative_returns_client = (1+daily_returns_client).cumprod()-1

    i=0
    cumulative_returns_client_portfolio=0
    for ticker in tickers:
        cumulative_returns_client_portfolio = cumulative_returns_client_portfolio+((1+daily_returns_client[ticker]).cumprod()-1)*client_portfolio[i]
        i += 1

    return prices_df_client, daily_returns_client, cumulative_returns_client_portfolio, closing_prices_client_portfolio_df

def get_MC_list_benchmark(prices_df_benchmark, MC_length_days):
   MC_list_benchmark =  MCSimulation(
        portfolio_data=prices_df_benchmark,
        weights=[0,0,0,1],
        num_simulation=50,
        num_trading_days=MC_length_days)
   return MC_list_benchmark

def get_MC_list_client(prices_df_client, client_portfolio, MC_length_days):
   MC_list_client =  MCSimulation(
        portfolio_data=prices_df_client,
        weights=client_portfolio,
        num_simulation=50,
        num_trading_days=MC_length_days)
   return MC_list_client

def get_closing_prices_benchmark(daily_prices_df):
    closing_prices_benchmark = pd.DataFrame()
    closing_prices_benchmark["QQQ"] = daily_prices_df["QQQ"]["close"]
    closing_prices_benchmark["SPY"] = daily_prices_df["SPY"]["close"]
    closing_prices_benchmark["IEF"] = daily_prices_df["IEF"]["close"]
    closing_prices_benchmark["DIA"] = daily_prices_df["DIA"]["close"]
    return closing_prices_benchmark

def get_cumulative_returns(daily_price_df):
    daily_returns=daily_price_df.pct_change().dropna()
    cumulative_returns = (1+daily_returns).cumprod()-1
    return cumulative_returns

def get_daily_returns(daily_price_df):
    daily_returns=daily_price_df.pct_change().dropna()
    return daily_returns