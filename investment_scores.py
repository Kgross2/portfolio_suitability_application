def score_calculator(investment_amount, annual_income, annual_expenses, investing_experience, income_stability, risk_level, investment_length, investment_strategy):
    risk_score = 0
    time_score = 0
    # investment_percent = investment_amount / annual_income
    # disposible_income = annual_income - annual_expenses
    # investment_ratio = disposible_income / investment_amount
    # if investment_percent < .40:
    #     risk_score += 100
    # elif investment_percent > .40 and investment_percent < .80:
    #     risk_score += 50
    # else:
    #     risk_score += 0 
    if investing_experience < 4:
        risk_score -= 10
    elif investing_experience > 4 and investing_experience < 9:
        risk_score += 0
    else:
        risk_score += 10
    if income_stability:
        risk_score += 0
    else:
        risk_score -= 40
    if risk_level == "Low":
        risk_score * .1
    elif risk_level == "Moderate":
        risk_score * .5
    elif risk_level == "High":
        risk_score * 1
    else:
        risk_score * 1.10
    if investment_length == "0-1":
        time_score += 25
    elif investment_length == "2-4":
        time_score += 50
    elif investment_length == "5-9":
        time_score += 75    
    else:
        time_score += 100

    return time_score, risk_score


def get_weights(risk_score, time_score):
    if risk_score < 20:
        weight = [.30,.36,.03,.09,0,.12,0,0.08,0]
    else:
        weight = [0,0,0,0,1,0,0,0,0,0]
    return weight