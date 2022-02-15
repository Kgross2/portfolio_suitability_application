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


    # #  Create an empty `closing_prices_df` DataFrame using Pandas
    # closing_prices_benchmark_df = pd.DataFrame()
    # # Populate the `closing_prices_df` DataFrame by accessing the `close` column from the `prices_df` DataFrame for both KO and TSLA .
    # closing_prices_benchmark_df["QQQ"] = prices_df_benchmark["QQQ"]["close"]
    # closing_prices_benchmark_df["SPY"] = prices_df_benchmark["SPY"]["close"]
    # closing_prices_benchmark_df["IEF"] = prices_df_benchmark["IEF"]["close"]
    # closing_prices_benchmark_df["DIA"] = prices_df_benchmark["DIA"]["close"]

    # daily_returns_benchmark_df = closing_prices_benchmark_df.pct_change().dropna()
    # cumulative_returns_benchmark_df = (1+daily_returns_benchmark_df).cumprod()-1

    return prices_df_benchmark #, closing_prices_benchmark_df, cumulative_returns_benchmark_df

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
    return daily_returns_client_portfolio_df, cumulative_returns_client_portfolio_df, closing_prices_client_portfolio_df 

def get_MC_simulation_benchmark(closing_prices_benchmark_df):
    weight = [0,0,0,1]
    MC_fiveyear = MCSimulation(
      portfolio_data = closing_prices_benchmark_df,
      weights = weight,
      num_simulation = 50,
      num_trading_days = 252*5
    )
    MC_cum = MC_fiveyear.calc_cumulative_return()
    MC_cum_mean = MC_cum.mean(axis=1)

    return MC_cum, MC_cum_mean

def get_tickers(port_profile):
    tickers = []

    if port_profile == "Fixed Income":
        tickers = ["AGG", "VCIT", "HYG", "BNDX"]
    elif port_profile == "Profile 1":
        tickers = ["AGG", "VCIT", "HYG", "BNDX", "VTV", "VXUS"]
    elif port_profile == "Profile 2":
        tickers = ["AGG", "VCIT", "HYG", "BNDX", "EMB", "VTV", "IJH", "VXUS"]
    elif port_profile == "Profile 3":
        tickers = ["AGG", "VCIT", "HYG", "BNDX", "EMB", "VTV", "IJH", "VB", "VXUS", "VWO"]
    elif port_profile == "Profile 4":
        tickers = ["AGG", "VCIT", "HYG", "BNDX", "EMB", "VTV", "IJH", "VB", "VXUS", "VWO"]
    elif port_profile == "Profile 5":
        tickers = ["VTV", "IJH", "VB", "VXUS", "VWO"]
    return tickers

def get_client_data(alpaca, tickers):
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
    return prices_df_client