
import questionary
from questionary.constants import Style, NO, YES, YES_OR_NO

custom_style=Style([
('answer', 'fg:#32cd32'),
('highlighted', 'fg:#32cd32 underline'),
('pointer', 'fg:#32cd32'),
('instruction', 'fg:#808080')
])

def basic_info():
    full_name = (questionary.text(
        "What's your name?",
        validate=lambda text: True if len(text) > 0 else "Please enter a valid name",
        style=custom_style
        ).ask())
    
    phone_number = (questionary.text(
        "What's your phone number?",
        instruction = '(No dashes only numbers)',   
        validate=lambda text: True if len(text) == 10 else "Please enter a valid 10-digit phone number",
        style=custom_style  
        ).ask())
    
    email_address = (questionary.text(
        "What's your email address?",
        validate=lambda text: True if len(text) > 0 else "Please enter a valid email address",
        style=custom_style
        ).ask())
    return full_name, phone_number, email_address
    
def financial_info():
    annual_income = (questionary.text(
        "What's your annual income?",
        validate=lambda text: True if int(text) > 0 else "Please enter a positive value",
        style=custom_style
        ).ask())
            # I want to require numeric values entered
        
    annual_expenses = (questionary.text(
        "What are your annual expenses?",
        validate=lambda text: True if int(text) > 0 else "Please enter a positive value",
        style=custom_style
        ).ask())
    
    income_stability = questionary.select(
        "Is your source of income stable?",
        choices=["Yes", "No"],
        instruction = '(Use arrow keys)',
        use_indicator= True,
        style=custom_style
        ).ask()

    # convert variable type
    annual_income = float(annual_income)
    annual_expenses = float(annual_expenses)
    income_stability = str(income_stability)

    return annual_income, annual_expenses, income_stability

def investment_info():
    investing_experience = questionary.text(
        "How many years of investing experience do you have?",
        validate=lambda text: True if int(text) > 0 and int(text) < 100 else "Please enter a valid value",
        style=custom_style
        ).ask()
    
    investment_amount = (questionary.text(
        "What is the amount you wish to start investing?",
        validate=lambda text: True if int(text) > 0 else "Please enter a positive value",
        style=custom_style
        ).ask())
    
    risk_level = questionary.select(
        "What is your level of risk?",
        choices=["Low", "Moderate", "High"],
        instruction = '(Use arrow keys)',
        use_indicator= True,
        style=custom_style
    ).ask()
    
    investment_strategy = questionary.select(
        "What type of investment strategy do you want?",
        choices=["Income", "Income/Growth/Value", "Growth/Value"],
        instruction = '(Use arrow keys)',
        use_indicator= True,
        style=custom_style
    ).ask()
    
    investment_length = questionary.select(
        "How long do you plan to invest the money in years?",
        choices=["0-1", "2-4", "5-9", "10+"],
        instruction = '(Use arrow keys)',
        use_indicator= True,
        style=custom_style
    ).ask()

    # convert variable type
    
    investing_experience = int(investing_experience)
    investment_amount = float(investment_amount)


    return investing_experience, investment_amount, risk_level, investment_strategy, investment_length

    