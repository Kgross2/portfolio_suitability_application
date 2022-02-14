# import required libraries

import fire
from questionary.constants import Style, NO, YES, YES_OR_NO
import os
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

#### Currently the following are not necessary.  DELETE WHEN CONFIRMED

#import sqlalchemy
#import requests
#import json
#from pathlib import Path
#import matplotlib
# from mailer import Mailer
#import questionary
#from questionary.constants import NO, YES, YES_OR_NO
#import sqlalchemy
#import hvplot.pandas

# import requiree local files
from client_questions import basic_info, investment_info, financial_info
from investment_scores import get_client_portfolio, score_calculator, get_MC_end_date
from etf_data import get_benchmark_data, get_MC_simulation_benchmark, get_tickers, get_client_portfolio_data
from client_output import create_pdf, create_info_img, intro_message, exit_message, clear_console   

# Load env
load_dotenv()
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

###  This is dummy data for testing to avoid having to enter info in Questionary for testing.  DELETE WHEN UNNEEDED
full_name = "Jacob"
phone_number = "713-555-7834"
email_address = "cdb@bcg.law"
annual_income = 10000
investing_experience = 10
investment_amount = 10000
annual_expenses = 5000
income_stability = "Yes"
risk_level = "Moderate"
investment_strategy = "Growth/Value"
investment_length = "1yr"
    
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

# get benchmark and client portfolio daily, cumulativ, and closing price dataframes
   daily_returns_benchmark_df, cumulative_returns_benchmark_df, closing_prices_benchmark_df = get_benchmark_data(alpaca)
   daily_returns_client_portfolio_df, cumulative_returns_client_portfolio_df, closing_prices_client_portfolio_df = get_client_portfolio_data(alpaca, tickers)
   
# run MC simulations on benchmark and client portfolios

######   MC_cum, MC_cum_mean = get_MC_simulation_benchmark(closing_prices_benchmark_df)

    
# use above data to create visualizations

   #cumulative_return_client_weight = cumulative_returns_benchmark["IEF"] * weight[0] + cumulative_returns_benchmark["LQD"] * weight[1] + cumulative_returns_benchmark["HYG"] * weight[2] + cumulative_returns_benchmark["IAGG"] * weight[3] + cumulative_returns_benchmark["EMHY"] * weight[4] + cumulative_returns_benchmark["SPY"] * weight[5] + cumulative_returns_benchmark["IJH"] * weight[6] + cumulative_returns_benchmark["IJR"] * weight[7] + cumulative_returns_benchmark["IXUS"] * weight[8] + cumulative_returns_benchmark["IEMG"] * weight[9]
   #get_MC_simulation(closing_prices_benchmark_df, )
   #create_info_img(full_name, phone_number, email_address, annual_income, income_stability, annual_expenses, investment_amount, investment_length, risk_level, investment_strategy)
   
# create the pdf from information above
   #create_pdf(full_name)

# print exit message for the client and terminate the program
   exit_message()




if __name__ == "__main__":
    fire.Fire(run)