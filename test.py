from client_questions import basic_info, investment_info, financial_info

import fire

def run():

   
   full_name, phone_number, email_address = basic_info()
   annual_income, annual_expenses, income_stability = financial_info()
   investing_experience, investment_amount, risk_level, investment_strategy, investment_length = investment_info()

   print(full_name, phone_number, email_address)
   print(annual_income, annual_expenses, income_stability)
   print(investing_experience, investment_amount, risk_level, investment_strategy, investment_length)


if __name__ == "__main__":
    fire.Fire(run)