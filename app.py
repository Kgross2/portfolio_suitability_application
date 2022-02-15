# import required libraries

import fire
from questionary.constants import Style, NO, YES, YES_OR_NO
import os
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# import required local files
from ui.client_questions import basic_info, investment_info, financial_info
from data.investment_scores import get_client_portfolio, score_calculator, get_MC_end_date
from data.etf_data import get_benchmark_data, get_MC_simulation_benchmark, get_tickers, get_client_portfolio_data
from ui.client_output import create_pdf, create_info_img, intro_message, exit_message, clear_console   

# Load env
load_dotenv()
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

# run port suitability app

def run():

# clear the console and launch intro message
   clear_console()
   intro_message()

# fire the client questions (basic, financial, investment)

   full_name, phone_number, email_address = basic_info()
   annual_income, annual_expenses, income_stability = financial_info()
   investing_experience, investment_amount, risk_level, investment_strategy, investment_length = investment_info()

# fire risk and time score calculator
   risk_score, time_score = score_calculator(investment_amount, annual_income, annual_expenses, investing_experience, income_stability, risk_level, investment_length, investment_strategy)

# get data for the client brochure - benchmark data
   closing_prices_benchmark_df, daily_returns_benchmark_df, cumulative_returns_benchmark_df = get_benchmark_data(alpaca)

# use risk and time score to select the clients portfolio profile, start date, and portfolio tickers 
   client_portfolio, port_profile, risk_score = get_client_portfolio(risk_score, time_score)
   tickers = get_tickers(port_profile)

# get benchmark and client portfolio daily, cumulative, and closing price dataframes
   daily_returns_benchmark_df, cumulative_returns_benchmark_df, closing_prices_benchmark_df = get_benchmark_data(alpaca)
   daily_returns_client_portfolio_df, cumulative_returns_client_portfolio_df, closing_prices_client_portfolio_df = get_client_portfolio_data(alpaca, tickers)
   
# run MC simulations on benchmark and client portfolios

######   MC_cum, MC_cum_mean = get_MC_simulation_benchmark(closing_prices_benchmark_df)

    
# use above data to create visualizations
  
# create the image and pdf from information above
   create_info_img(full_name, phone_number, email_address, annual_income, income_stability, annual_expenses, investment_amount, investment_length, risk_level, investment_strategy)
   create_pdf(full_name)

# print exit message for the client and terminate the program
   exit_message(full_name)

if __name__ == "__main__":
    fire.Fire(run)