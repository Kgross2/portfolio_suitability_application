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
from investment_scores import score_calculator, get_weights
from etf_data import get_benchmark_data, get_MC_simulation
from client_output import create_pdf, create_info_img

# Load env
load_dotenv()
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

###  This is dummy data for testing to avoid having to enter info in Questionary for testing.  DELETE WHEN UNNEEDED
full_name = "John Jenkins"
phone_number = "713-555-7834"
email_address = "cdb@bcg.law"
annual_income = 100000
investing_experience = 4
investment_amount = 10000
annual_expenses = 50000
income_stability = "YES"
risk_level = "Low"
investment_strategy = "Value"
investment_length = "0-1"
    
# run port suitability app

def run():

# # fire the client questions (basic, financial, investment)
#    full_name, phone_number, email_address = basic_info()
#    annual_income, annual_expenses, income_stability = financial_info()
#    investing_experience, investment_amount, risk_level, investment_strategy, investment_length = investment_info()
# fire score calculator
   risk_score, time_score = score_calculator(investment_amount, annual_income, annual_expenses, investing_experience, income_stability, risk_level, investment_length, investment_strategy)

   closing_prices_benchmark_df, daily_returns_benchmark_df, cumulative_returns_benchmark = get_benchmark_data(alpaca)

   #print(daily_returns_benchmark_df["IXUS"])
   #print(risk_score, time_score)

   weight = get_weights(risk_score, time_score)
   
   cumulative_return_client_weight = cumulative_returns_benchmark["IEF"] * weight[0] + cumulative_returns_benchmark["LQD"] * weight[1] + cumulative_returns_benchmark["HYG"] * weight[2] + cumulative_returns_benchmark["IAGG"] * weight[3] + cumulative_returns_benchmark["EMHY"] * weight[4] + cumulative_returns_benchmark["SPY"] * weight[5] + cumulative_returns_benchmark["IJH"] * weight[6] + cumulative_returns_benchmark["IJR"] * weight[7] + cumulative_returns_benchmark["IXUS"] * weight[8] + cumulative_returns_benchmark["IEMG"] * weight[9]
   
   get_MC_simulation(closing_prices_benchmark_df, weight)

   create_info_img(full_name, phone_number, email_address, annual_income, income_stability, annual_expenses, investment_amount, investment_length, risk_level, investment_strategy)
   
   create_pdf(full_name)





if __name__ == "__main__":
    fire.Fire(run)