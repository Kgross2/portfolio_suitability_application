import pandas as pd
# risk score assessment based upon questionary information 
def score_calculator(investment_amount, annual_income, annual_expenses, investing_experience, income_stability, risk_level, investment_length, investment_strategy):
        risk_score = 0
        
        investment_percent = investment_amount / annual_income
        
        # investment percentage is used to establish if the investment amount is significant
        # to the individuals annual income
        if investment_percent < .40:
            risk_score += 10
        elif investment_percent > .40:
            risk_score -= -10
        # investing experience is used to help establish a risk score based upon the clients experience
        if investing_experience < 4:
            risk_score -= 10
        elif investing_experience > 4 and investing_experience < 9:
            risk_score += 0
        else:
            risk_score += 10
        # income stability is used to help establish if the investment amount is significant to the client
        # and how protected the investment should be
        if income_stability == 'Yes':
            risk_score += 0
        else:
            risk_score -= 40
        # risk level is used to determine the amount of risk the client is comfortable with
        if risk_level == "Low":
            risk_score += 0
        elif risk_level == "Moderate":
            risk_score += 25
        elif risk_level == "High":
            risk_score += 50


        # investment strategy is used to determine the strategy used in the clients portfolio

        if investment_strategy == "Income":
            risk_score = 0
        elif investment_strategy == "Income/Growth/Value":
            risk_score += 20
        elif investment_strategy == "Growth/Value":
            risk_score += 40

        return risk_score

# defines the clients portfolio as well as the weights in each portfolio
def get_client_portfolio(risk_score):
    fixed_income = [.40, .45, .04, .11]
    profile_1 = [.32, .36, .03, .09, .12, .08]
    profile_2 = [.21, .23, .04, .08, .04, .18, .06, .16]
    profile_3 = [.11, .23, .04, .08, .04, .24, .09, .03, .20, .04]
    profile_4 = [.05, .06, .03, .03, .03, .32, .10, .06, .26, .06]
    profile_5 = [.40, .13, .07, .33, .07]

    # iterates through each portfolio in order to match the risk score with the desired portfolio
    if risk_score in range(-100, 11):

        client_portfolio = fixed_income
        port_profile = "Fixed Income"
    elif risk_score in range(11, 21):
        client_portfolio = profile_1
        port_profile = "Profile 1"
    elif risk_score in range(21, 41):
        client_portfolio = profile_2
        port_profile = "Profile 2"
    elif risk_score in range(41, 61):
        client_portfolio = profile_3
        port_profile = "Profile 3"
    elif risk_score in range(61, 81):
        client_portfolio = profile_4
        port_profile = "Profile 4"
    elif risk_score:
        client_portfolio = profile_5
        port_profile = "Profile 5"

    return client_portfolio, port_profile, risk_score
# uses investment length to establish number of trading days in the Monte Carlo simulation
def get_MC_length(investment_length):
    MC_length_days = []
    if investment_length == "0-1":
        MC_length_days = 252*1
        MC_length_str = "1 year"
    if investment_length == "2-4":
        MC_length_days = 252*4
        MC_length_str = "4 years"
    if investment_length == "5-9":
        MC_length_str = "9 years"
        MC_length_days = 252*9
    if investment_length == "10+":
        MC_length_days = 252*20
        MC_length_str = "20 years"
    return MC_length_days, MC_length_str