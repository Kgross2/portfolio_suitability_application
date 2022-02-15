# import required libraries

import fire
from questionary.constants import Style, NO, YES, YES_OR_NO
import os
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from data.MCForecastTools import MCSimulation

# import required local files
from ui.client_questions import basic_info, investment_info, financial_info
from data.investment_scores import get_client_portfolio, score_calculator, get_MC_end_date
from data.etf_data import get_benchmark_data, get_MC_simulation_benchmark, get_tickers, get_client_portfolio_data, get_client_data
from ui.client_output import create_pdf, create_info_img, intro_message, exit_message, clear_console   

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

# # fire the client questions (basic, financial, investment)

#    full_name, phone_number, email_address = basic_info()
#    annual_income, annual_expenses, income_stability = financial_info()
#    investing_experience, investment_amount, risk_level, investment_strategy, investment_length = investment_info()

# fire risk and time score calculator
   risk_score, time_score = score_calculator(investment_amount, annual_income, annual_expenses, investing_experience, income_stability, risk_level, investment_length, investment_strategy)

#, closing_prices_benchmark_df, daily_returns_benchmark_df, cumulative_returns_benchmark_df
# use risk and time score to select the clients portfolio profile, start date, and portfolio tickers 
   client_portfolio, port_profile, risk_score = get_client_portfolio(risk_score, time_score)
   tickers = get_tickers(port_profile)


# get data for the client brochure - benchmark data and client data
   prices_df_benchmark = get_benchmark_data(alpaca)
   prices_df_client = get_client_data(alpaca, tickers)

   MC_list_benchmark =  MCSimulation(
        portfolio_data=prices_df_benchmark,
        weights=[0,0,0,1],
        num_simulation=50,
        num_trading_days=252*3)
    
   print(MC_list_benchmark.calc_cumulative_return())
   MC_list_benchmark.plot_simulation()

   MC_list_client =  MCSimulation(
        portfolio_data=prices_df_client,
        weights=client_portfolio,
        num_simulation=50,
        num_trading_days=252*3)
    
   MC_list_client.calc_cumulative_return()
   MC_list_client.plot_simulation()

   print(MC_list_client)






# use above data to create visualizations
  
# create the image and pdf from information above
   create_info_img(full_name, phone_number, email_address, annual_income, income_stability, annual_expenses, investment_amount, investment_length, risk_level, investment_strategy)
   create_pdf(full_name)

# print exit message for the client and terminate the program
   exit_message(full_name)

if __name__ == "__main__":
    fire.Fire(run)