from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont
import os

from numpy import cdouble


def create_info_img(full_name, phone_number, email_address, annual_income, income_stability, annual_expenses, investment_amount, investment_length, risk_level, investment_strategy):
    # name of the file to save
    filename = "./img/clientdata.png"
    fnt = ImageFont.truetype('../img/Arial.ttf', 12)
    # create new image
    image = Image.new(mode = "RGB", size = (300,200), color = (39,70,132))
    draw = ImageDraw.Draw(image)
    draw.text((15,15), "Full Name:", font=fnt, fill=(255,255,255))
    draw.text((160,15), full_name, font=fnt, fill=(255,255,255))
    draw.text((15,30), "Phone Number:", font=fnt, fill=(255,255,255))
    draw.text((160,30), phone_number, font=fnt, fill=(255,255,255))
    draw.text((15,45), "Email:", font=fnt, fill=(255,255,255))
    draw.text((160,45), email_address, font=fnt, fill=(255,255,255))
    draw.text((15,60), "Annual Income", font=fnt, fill=(255,255,255))
    draw.text((160,60), str(annual_income), font=fnt, fill=(255,255,255))
    draw.text((15,75), "Income Stability", font=fnt, fill=(255,255,255))
    draw.text((160,75), income_stability, font=fnt, fill=(255,255,255))
    draw.text((15,90), "Annual Expenses", font=fnt, fill=(255,255,255))
    draw.text((160,90), str(annual_expenses), font=fnt, fill=(255,255,255))
    draw.text((15,105), "Investment Amount:", font=fnt, fill=(255,255,255))
    draw.text((160,105), str(investment_amount), font=fnt, fill=(255,255,255))
    draw.text((15,120), "Risk Tolerance", font=fnt, fill=(255,255,255))
    draw.text((160,120), risk_level, font=fnt, fill=(255,255,255))
    draw.text((15,135), "Investment Time Horizon", font=fnt, fill=(255,255,255))
    draw.text((160,135), investment_length, font=fnt, fill=(255,255,255))
    draw.text((15,150), "Investment Strategy", font=fnt, fill=(255,255,255))
    draw.text((160,150), investment_strategy, font=fnt, fill=(255,255,255))
    image.save(filename)
    return


def create_pdf(full_name, MC_benchmark_summary, MC_client_summary):
    WIDTH = 215.9
    HEIGHT = 279.4
    pdf = FPDF('P', 'mm', 'Letter')
    # page 1
    pdf.add_page()
    pdf.set_font('Arial', '', 21)
    pdf.image("./img/letterhead1.png", 0, 0, WIDTH)
    pdf.ln(10)
    pdf.set_left_margin(100)
    pdf.set_text_color(255, 255, 255)
    pdf.write(10, f"Portfolio Suitability Report")
    pdf.set_left_margin(10)
    pdf.ln(45)
    pdf.set_text_color(100)
    pdf.set_font('Arial', '', 21)
    pdf.write(10, f"Portfolio Report for {full_name}")
    pdf.ln(15)
    pdf.set_text_color(100)
    pdf.set_font('Arial', '', 13)
    pdf.multi_cell(WIDTH-20,5, f"Thank you for trusting our team with your information.  We believe that this report will be beneficial and assist you on your financial journey.  In the pages that follow, you will find educational material custom tailored to your risk tolerance, investment horizon, and preferred investment strategy.  Our investment advisor will follow up with you in a couple of days to answer any questions that you have and assist you in implementing your investment plan.  Welcome to the JACK Investment family.", border=1)
    pdf.set_font('Arial', '', 12)
    pdf.ln(16)
    pdf.multi_cell(WIDTH/2-10,5, "In the pages that follow, you will find your Risk Assessment Score, your Investment Horizon Score, and your Investment Strategy.  This report has been created using cutting edge analysis to provide you with the best investment alternatives based upon your criteria.  If any of the information in the chart to the right is incorrect, please notify your account representative as this report is created using this financial and investment data.", border = 0)
    pdf.image("./img/clientdata.png", x = 110, y = 120, w = WIDTH/2-10)
    pdf.ln(18)
    pdf.set_left_margin(WIDTH/2+5)
    pdf.multi_cell(WIDTH/2-12,5, "To the left, you will see a pie chart that shows the percentage of the custom portfolio created for you by our system.  The ETFs in this chart are blended together to meet your risk tolerance as well as your financial data.  The composition of this portfolio is based on traditional stock market allocations.  In the pages that follow, we will show you how this portfolio has performed in the past relative to the market as a whole and how simulations predict it will react for your time horizon.  ", border = 0)
    pdf.image("img/pie_chart_client_portfolio.png", x = 8, y = 180, w = WIDTH/2-10)
    pdf.set_left_margin(10)
    pdf.ln(5)
    pdf.set_font('Arial', '', 8)
    pdf.multi_cell(WIDTH-20,3, "Past performance is not a guarantee of future return, nor is it necessarily indicative of future performance. Keep in mind investing involves risk. The value of your investment will fluctuate over time and you may gain or lose money. You should take independent financial advice from a professional in connection with, or independently research and verify, any information that you review.", border = 1)
    # page 2
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.image("./img/letterhead2.png", 0, 0, WIDTH)
    pdf.ln(10)
    pdf.set_left_margin(10)
    pdf.image("img/portfolio_theory_table.png", x = 10, y = 10, w = WIDTH-20)
    pdf.ln(77)
    pdf.multi_cell(WIDTH-20,5, "The table above shows the different profiles and how those portfolios distribute risk for the profiles.  For example, the Fixed Income Profile has no equity portion in the portfolio while Portfolio 5 has almost exclusively equities.", border = 0)
    pdf.ln(2)
    pdf.multi_cell(WIDTH/2-10,5, "The goal of creating these portfolios is to balance risk and return.  As you can see here, the IEF fund (shown in blue) has significantly lower volitility than the QQQ (shown in green).  But as we will see in our next chart, the QQQ's return has been significantly higher as well.  By blending ETFs together, your broker at JACK financial can reduce volitility while improving your returns.", border = 0)
    pdf.image("./img/45_day_vol_benchmark.png", x = 110, y = 110, w = WIDTH/2-10)
    pdf.output('./pdf/portfolio_suitability_report.pdf', 'F')
    return

def intro_message():
    print("    ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╙╙╙╙╙╙╙╙╬╬╬╬╬╬╬╬╬╜╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╝▀╙╙╙╙▀╣╬╬╩╬╬▓╙▀▀▀▀▀╙▓╬╬╬╬╙╙╙╙╙║╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬▓   ╬╬╬╬╬╬╬╬╬╬Γ ╙╬╬╬╬╬╬╬╬╬╬╬▀  ╔▓╬╬╬╬╬▓,  ╬╬╬╬╬   ╬╬╬╬╬╬▓╜ é╣╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬▌   ╬╬╬╬╬╬╬╬╬▌   ╚╬╬╬╬╬╬╬╬▓   ▓╬╬╬╬╬╬╬╬╬L ╬╬╬╬╬   ╬╬╬╬▓╜,#╣╬╬╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬▌   ╬╬╬╬╬╬╬╬▓ ▓   ╟╬╬╬╬╬╬╬   @╬╬╬╬╬╬╬╬╬╬╬,╬╬╬╬╬   ╬╬╝`╒▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬▌   ╬╬╬╬╬╬╬╬ å╬▓   ▓╬╬╬╬╬Γ   ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬   ▀  ▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬▌   ╬╬╬╬╬╬╬Γ╒╬╬╬▌   ╬╬╬╬╬Γ   ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬   ╦   ╙╣╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬▌   ╬╬╬╬╬╬▌ ╝╝╝╝╝-  ╘╬╬╬╬▌   ╣╬╬╬╬╬╬╬╬╬╬╬╬▓╬╬╬╬   ╬▓µ   ╚╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬▌   ╬╬╬╬╬▓ ▓▓▓▓▓▓▓   ╚╬╬╬╬µ  ╘╬╬╬╬╬╬╬╬╬╬╬Γ@╬╬╬╬   ╬╬╬▓┐   ╚╬╬╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬▌   ╬╬╬╬╬ ║╬╬╬╬╬╬╬▌   ╟╬╬╬╬╗  ╙╣╬╬╬╬╬╬╬╬▀ ║╬╬╬╬   ╬╬╬╬╬▓,   ╫╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╣╣╬▌  ▐╬╬╣▓` ╣╣╬╬╬╬╝╝╝─   ╝╝╣╬╬╬▌, ╙╝╣╣╣╝╜ ╔ ║╬╬╣▓   ╣╣╣╬╬╬╣▌   `╝╣╣╬╬╬╬╬")
    print("    ╬╬╬╬╬╬   ║▌  ▓╬▓▓▓▓▓▓▓▓╬╬╬▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬▓▓▓▓▓╬╬╬▓▓╬▓▓▓▓▓▓▓▓▓╬╬╬▓▓▓▓▓▓▓▓▓╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╗,,╠╓Φ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("    ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("Hello.  Welcome to the JACK Financial Portfolio Suitability Application.  This application will ask you a series of questions and then create a portfolio plan for you.  Upon completion, one of our brokers will reach out to you to schedule a time to review the recommendations.  Let's get started by getting to know you better.")

def exit_message(full_name):
    print(f"Thank you {full_name} for using our service.  Your information has been processed and our broker team will be in touch with you soon." )


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
