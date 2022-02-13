import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import os
from MCForecastTools import MCSimulation


# Load env
load_dotenv()
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

def get_benchmark_data(alpaca):
    # Determine info for SPY, QQQ, IEF, and client selections
    # Use Alpaca to pull last 3 years data for SPY, QQQ, IEF, and Possible Client Selections
    # Set the ticker symbols
    tickers = ["QQQ","SPY", "IEF", "DIA", "LQD", "HYG", "IAGG", "EMHY", "IJH", "IJR", "IXUS", "IEMG"]
    # Set timeframe to '1D'
    timeframe = "1D"
    # Set start and end datetimes of 3 years.
    start_date = pd.Timestamp("2019-02-09", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2022-02-9", tz="America/New_York").isoformat()
    # Set number of rows to 1000 to retrieve the maximum amount of rows
    limit_rows = 1000
    # Get 3 year's worth of historical data for tickers
    prices_df_benchmark = alpaca.get_barset(
      tickers,
      timeframe,
      start=start_date,
      end=end_date,
      limit=limit_rows
    ).df

    #  Create an empty `closing_prices_df` DataFrame using Pandas
    closing_prices_benchmark_df = pd.DataFrame()
    # Populate the `closing_prices_df` DataFrame by accessing the `close` column from the `prices_df` DataFrame for both KO and TSLA .
    closing_prices_benchmark_df["QQQ"] = prices_df_benchmark["QQQ"]["close"]
    closing_prices_benchmark_df["SPY"] = prices_df_benchmark["SPY"]["close"]
    closing_prices_benchmark_df["IEF"] = prices_df_benchmark["IEF"]["close"]
    closing_prices_benchmark_df["DIA"] = prices_df_benchmark["DIA"]["close"]
    closing_prices_benchmark_df["LQD"] = prices_df_benchmark["LQD"]["close"]
    closing_prices_benchmark_df["HYG"] = prices_df_benchmark["HYG"]["close"]
    closing_prices_benchmark_df["IAGG"] = prices_df_benchmark["IAGG"]["close"]
    closing_prices_benchmark_df["EMHY"] = prices_df_benchmark["EMHY"]["close"]
    closing_prices_benchmark_df["IJH"] = prices_df_benchmark["IJH"]["close"]
    closing_prices_benchmark_df["IJR"] = prices_df_benchmark["IJR"]["close"]
    closing_prices_benchmark_df["IXUS"] = prices_df_benchmark["IXUS"]["close"]
    closing_prices_benchmark_df["IEMG"] = prices_df_benchmark["IEMG"]["close"]

    daily_returns_benchmark_df = closing_prices_benchmark_df.pct_change().dropna()

    cumulative_returns_benchmark = (1+daily_returns_benchmark_df).cumprod()-1

    return daily_returns_benchmark_df, cumulative_returns_benchmark, closing_prices_benchmark_df 

def get_MC_simulation(closing_prices_benchmark_df, weight):
    MC_fiveyear = MCSimulation(
      portfolio_data = closing_prices_benchmark_df,
      weights = weight,
      num_simulation = 50,
      num_trading_days = 252*5
    )
    MC_cum = MC_fiveyear.calc_cumulative_return()

    MC_cum_mean = MC_cum.mean(axis=1)

    # Plot simulation outcomes
    MC_sim_line_plot = MC_fiveyear.plot_simulation()
    # Save the plot for future use
    MC_sim_line_plot.get_figure().savefig("img/mc.png", bbox_inches="tight")

    return MC_cum, MC_cum_mean
