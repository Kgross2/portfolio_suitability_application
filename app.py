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
from data.investment_scores import get_client_portfolio, score_calculator, get_MC_length
from data.etf_data import get_benchmark_data, get_tickers, get_client_portfolio_data, get_client_data, get_MC_list_benchmark, get_MC_list_client, get_daily_returns, get_cumulative_returns, get_closing_prices_benchmark
from ui.vis import save_vis_daily_return_distribution_benchmark, save_vis_cumulative_return_distribution_benchmark, save_45_day_rolling_volitility_benchmark, save_vis_daily_return_distribution_client, save_vis_cumulative_return_distribution_client, save_45_day_rolling_volitility_client, save_vis_cumulative_return_benchmark_client, plot_mc_sp, plot_mc_client, pie_chart_client_portfolio   
from ui.client_output import clear_console, intro_message, create_info_img, exit_message, create_pdf     

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

# use risk and time score to select the clients portfolio profile, start date, and portfolio tickers 
   client_portfolio, port_profile, risk_score = get_client_portfolio(risk_score, time_score)
   tickers = get_tickers(port_profile)
   MC_length_days, MC_length_str = get_MC_length(investment_length)

# get data for the client brochure - benchmark data and client data
   prices_df_benchmark = get_benchmark_data(alpaca)
   closing_prices_benchmark_df = get_closing_prices_benchmark(prices_df_benchmark)
   daily_returns_df_benchmark = get_daily_returns(closing_prices_benchmark_df)
   cumulative_returns_df_benchmark = get_cumulative_returns(closing_prices_benchmark_df)

   prices_df_client_portfolio, daily_returns_client_portfolio_df, cumulative_returns_client_portfolio_df, closing_prices_client_portfolio_df = get_client_data(alpaca, tickers, client_portfolio)

# run Monte Carlo simulations for benchmark and client
   MC_list_benchmark = get_MC_list_benchmark(prices_df_benchmark, MC_length_days) 
   MC_list_client = get_MC_list_client(prices_df_client_portfolio, client_portfolio, MC_length_days)

   MC_benchmark_summary = MC_list_benchmark.summarize_cumulative_return()
   MC_client_summary = MC_list_client.summarize_cumulative_return()

# create visuals
   save_vis_daily_return_distribution_benchmark(daily_returns_df_benchmark)
   save_vis_cumulative_return_distribution_benchmark(cumulative_returns_df_benchmark)
   save_45_day_rolling_volitility_benchmark(daily_returns_df_benchmark)   
   save_vis_daily_return_distribution_client(daily_returns_client_portfolio_df)
   save_vis_cumulative_return_distribution_client(cumulative_returns_client_portfolio_df)
   save_45_day_rolling_volitility_client(daily_returns_client_portfolio_df)  
   save_vis_cumulative_return_benchmark_client(cumulative_returns_df_benchmark, cumulative_returns_client_portfolio_df) 
   plot_mc_sp(MC_list_benchmark)
   plot_mc_client(MC_list_client)
   pie_chart_client_portfolio(client_portfolio, tickers)

# create the image and pdf from information above
   create_info_img(full_name, phone_number, email_address, annual_income, income_stability, annual_expenses, investment_amount, investment_length, risk_level, investment_strategy)
   create_pdf(full_name, MC_benchmark_summary, MC_client_summary)

# print exit message for the client and terminate the program
   exit_message(full_name)

if __name__ == "__main__":
    fire.Fire(run)