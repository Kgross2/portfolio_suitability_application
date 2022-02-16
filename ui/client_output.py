from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont
import os

from numpy import cdouble


def create_info_img(full_name, phone_number, email_address, annual_income, income_stability, annual_expenses, investment_amount, investment_length, risk_level, investment_strategy):
    # name of the file to save
    filename = "./img/clientdata.png"
    fnt = ImageFont.truetype('../img/Arial.ttf', 11)
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

def create_MC_comparison_img(MC_benchmark_summary, MC_client_summary, investment_amount):
    # name of the file to save
    filename = "./img/MC_comparison.png"
    fnt = ImageFont.truetype('../img/Arial.ttf', 15)

    # # create new image
    
    image = Image.new(mode = "RGB", size = (705,148), color = (39,70,132))
    draw = ImageDraw.Draw(image)
    draw.rectangle([0,0,235,147], fill=(255,255,255), outline=(0,0,0), width=1)
    draw.rectangle([235,0,470,147], fill=(224,224,224), outline=(0,0,0), width=1)
    draw.rectangle([470,0,704,147], fill=(204,229,255), outline=(0,0,0), width=1)

    draw.text((20,30), "Average Return", font=fnt, fill=(0,0,0))
    draw.text((20,50), "Standard Deviation", font=fnt, fill=(0,0,0))
    draw.text((20,70), "Lowest Return", font=fnt, fill=(0,0,0))
    draw.text((20,90), "95% CI Low Return", font=fnt, fill=(0,0,0))
    draw.text((20,110), "95% CI High Return", font=fnt, fill=(0,0,0))
    draw.text((20,130), f"Avg. Return (${investment_amount:,.2f})", font=fnt, fill=(0,0,0))

    draw.text((275,10), "S&P 500 Simulation", font=fnt, fill=(0,0,0))
    draw.text((315,30), f"{MC_benchmark_summary[1]*100:.2f}%", font=fnt, fill=(0,0,0))
    draw.text((315,50), f"{MC_benchmark_summary[2]:.2f}", font=fnt, fill=(0,0,0))
    draw.text((315,70), f"{MC_benchmark_summary[3]*100:.2f}%", font=fnt, fill=(0,0,0))
    draw.text((315,90), f"{MC_benchmark_summary[8]*100:.2f}%", font=fnt, fill=(0,0,0))
    draw.text((315,110), f"{MC_benchmark_summary[9]*100:.2f}%", font=fnt, fill=(0,0,0))
    draw.text((315,130), f"$ {(MC_benchmark_summary[2]+1)*(investment_amount):,.2f}", font=fnt, fill=(0,0,0))

    draw.text((500,10), "Client Portfolio Simulation", font=fnt, fill=(0,0,0))
    draw.text((550,30), f"{MC_client_summary[1]*100:.2f}%", font=fnt, fill=(0,0,0))
    draw.text((550,50), f"{MC_client_summary[2]:.2f}", font=fnt, fill=(0,0,0))
    draw.text((550,70), f"{MC_client_summary[3]*100:.2f}%", font=fnt, fill=(0,0,0))
    draw.text((550,90), f"{MC_client_summary[8]*100:.2f}%", font=fnt, fill=(0,0,0))
    draw.text((550,110), f"{MC_client_summary[9]*100:.2f}%", font=fnt, fill=(0,0,0))
    draw.text((550,130), f"$ {(MC_client_summary[2]+1)*(investment_amount):,.2f}", font=fnt, fill=(76,153,0))



    image.save(filename)
    return


def create_pdf(full_name, port_profile, MC_length_str):
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
    pdf.multi_cell(WIDTH-20,5, f"Thank you for trusting our team with your information.  We believe that this report will be beneficial and assist you on your financial journey.  Included, you will find educational material custom tailored to your risk tolerance, investment horizon, and preferred investment strategy.  Some of this may be new to you.  Don't worry.  Our investment advisors will be happy answer any questions that you have and assist you in implementing your investment plan.  Welcome to the JACK Investment family.", border=1)
    pdf.set_font('Arial', '', 12)
    pdf.ln(16)
    pdf.multi_cell(WIDTH/2-10,5, "In the pages that follow, you will see how your answers were used to create a portfolio of exchange traded funds (ETFs).  This report has been created using cutting edge analysis to provide you with the best investment alternatives based upon your unique criteria.  So please, check the chart to the right.  If any of the information in the chart is incorrect, please notify your account representative as this report is created using this financial and investment data.", border = 0)
    pdf.image("./img/clientdata.png", x = 110, y = 120, w = WIDTH/2-10)
    pdf.ln(18)
    pdf.set_left_margin(WIDTH/2+5)
    pdf.multi_cell(WIDTH/2-12,5, "To the left, you will see a pie chart that shows the selection and percentage of ETFs in your custom portfolio.  The ETFs in this chart are blended together to meet your risk tolerance as well as your financial data.  The composition of this portfolio is based on traditional stock market allocations.  In the pages that follow, we will show you how this portfolio has performed in the past relative to the market as a whole and how simulations predict it will performn.", border = 0)
    pdf.image("img/pie_chart_client_portfolio.png", x = 8, y = 180, w = WIDTH/2-10)
    pdf.set_left_margin(10)
    pdf.ln(5)
    pdf.set_font('Arial', '', 8)
    pdf.multi_cell(WIDTH-20,3, "Past performance is not a guarantee of future results, nor is it necessarily indicative of future performance. Keep in mind that investing involves risk. The value of your investment will fluctuate over time and you may gain or lose money. You should take independent financial advice from a professional in connection with, or independently research and verify, any information that you review.  If you have questions, please contact a JACK Financial Advisor.", border = 1)

    # page 2
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.image("./img/letterhead2.png", 0, 0, WIDTH)
    pdf.ln(10)
    pdf.set_left_margin(10)
    pdf.image("img/portfolio_theory_table.png", x = 10, y = 10, w = WIDTH-20)
    pdf.ln(77)
    pdf.multi_cell(WIDTH-20,5, f"The table above shows the different profiles and how those portfolios distribute risk for the profiles.  For example, the Fixed Income Profile has no equity portion in the portfolio while Portfolio 5 has almost exclusively equities.  Based on your responses, {port_profile} has been recommended.", border = 0)
    pdf.ln(4)
    pdf.multi_cell(WIDTH/2-10,5, f"The goal of creating these portfolios is to balance risk and return.  Volitility is a measure of risk.  So, by reducing volitility, we can reduce risk.  As you can see here, the light greeen lines represent the components of the {port_profile} portfolio.  The darker green line is the volitility of the combined portfolio.  By combining multiple ETFs, we can moderate volitility.", border = 0)
    pdf.image("./img/45_day_vol_client.png", x = 110, y = 112, w = WIDTH/2-10)
    pdf.ln(4)
    pdf.multi_cell(WIDTH/2-10,5, f"When the {port_profile} is compared to the traditional stock benchmarks (QQQ, S&P 500, U.S. Bonds, and the Dow Jones), the {port_profile} portfolio has a lower volitility than the equity benchmarks.  But this reduced volitility also reduces the expected return. By listening to our clients, we can blend ETFs together, reducing volitility while improving your returns.", border = 0)
    pdf.ln(4)
    pdf.multi_cell(WIDTH/2-10,5, f"We would love to discuss this with you in detail whenever you are available.", border = 0)
    pdf.ln(4)
    pdf.multi_cell(WIDTH/2-10,5, f"But, now that we have touched on the volitility or risk of the {port_profile} profile, let us turn to the past and future expected returns for the {port_profile} portfolio.", border = 0)
    pdf.image("./img/45_day_vol_benchmark.png", x = 110, y = 185, w = WIDTH/2-10)

    # page 3
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.image("./img/letterhead2.png", 0, 0, WIDTH)
    pdf.image("img/cumulative_return_benchmark.png", x = 110, y = 20, w = WIDTH/2-20)
    pdf.image("img/cumulative_return_benchmark_client.png", x = 110, y = 80, w = WIDTH/2-20)
    pdf.image("img/mc_sp.png", x = 10, y = 152, w = WIDTH/2-20)
    pdf.image("img/mc_client.png", x = 110, y = 152, w = WIDTH/2-20)
    pdf.image("img/MC_comparison.png", x = 20, y = 222, w = 176)
    pdf.ln(20)
    pdf.set_left_margin(10)
    pdf.multi_cell(WIDTH/2-10,5, f"The chart to the right shows the cumulative returns of the traditional benchmarks (QQQ, S&P 500, U.S. Bonds, and the Dow Jones) over the last three years.  The benchmark with the highest return is the QQQ, but as we saw above, this high-return index is very volitile.  By contrast, the traditionally stable bond fund (IEF) significantly underperforms the equity markets.", border = 0)
    pdf.ln(4)
    pdf.multi_cell(WIDTH/2-10,5, f"The second chart compares the historic returns of the {port_profile} portfolio.  Recall that this portfolio is balanced to reduce volitility (and therefore risk).  It is therefore no surprise that the return for the combined portfolio is lower than the less diversified S&P 500, which is composed of only big U.S. companies.", border = 0)
    pdf.ln(4)
    pdf.multi_cell(WIDTH/2-10,5, f"When you meet with your JACK Financial Advisor, be sure to raise your questions about risk and return as it is critical that there is good communication between the client and the advisor to make sure that expectations are set and exceeded.", border = 0)
    pdf.ln(3)
    pdf.multi_cell(WIDTH-20,5, f"The tables below show the simulated future performance of the S&P 500 and the {port_profile} portfolio.", border = 0)
    pdf.ln(50)
    pdf.multi_cell(WIDTH-20,5, f"These simulations are performed to give some guidance about the future.  We have run a simulation over {MC_length_str}.  In the table below, we compare the simulated outcomes.  These results will give you and your JACK Financial Advisor a good starting place for conversations about what to expect from your {port_profile} portfolio in the coming years.", border = 0)

    # page 4
    pdf.add_page()
    pdf.set_font('Arial', '', 16)
    pdf.image("./img/letterhead2.png", 0, 0, WIDTH)
    pdf.multi_cell(WIDTH-20,5, f"Appendix - Portfolio Pie Chart", border = 0, align = "Center")
    pdf.image("img/pie_chart_client_portfolio.png", x = 10, y = 75, w = WIDTH-20)

    # page 5
    pdf.add_page()
    pdf.set_font('Arial', '', 16)
    pdf.image("./img/letterhead2.png", 0, 0, WIDTH)
    pdf.multi_cell(WIDTH-20,5, f"Appendix - Cumulative Return of Benchmark Portfolios", border = 0, align = "Center")
    pdf.image("img/cumulative_return_benchmark.png", x = 10, y = 75, w = WIDTH-20)
 
    # page 6
    pdf.add_page()
    pdf.set_font('Arial', '', 16)
    pdf.image("./img/letterhead2.png", 0, 0, WIDTH)
    pdf.multi_cell(WIDTH-20,5, f"Appendix - Cumulative Return of Client and Benchmark Portfolios", border = 0, align = "Center")
    pdf.image("img/cumulative_return_benchmark_client.png", x = 10, y = 75, w = WIDTH-20)
 
    # page 7
    pdf.add_page()
    pdf.set_font('Arial', '', 16)
    pdf.image("./img/letterhead2.png", 0, 0, WIDTH)
    pdf.multi_cell(WIDTH-20,5, f"Appendix - 45 Day Volatility Benchmark Portfolios", border = 0, align = "Center")
    pdf.image("img/45_day_vol_benchmark.png", x = 10, y = 75, w = WIDTH-20)
 
    # page 8
    pdf.add_page()
    pdf.set_font('Arial', '', 16)
    pdf.image("./img/letterhead2.png", 0, 0, WIDTH)
    pdf.multi_cell(WIDTH-20,5, f"Appendix - 45 Day Volatility Client Portfolios", border = 0, align = "Center")
    pdf.image("img/45_day_vol_client.png", x = 10, y = 75, w = WIDTH-20)

    # page 9
    pdf.add_page()
    pdf.set_font('Arial', '', 16)
    pdf.image("./img/letterhead2.png", 0, 0, WIDTH)
    pdf.multi_cell(WIDTH-20,5, f"Appendix - Portfolio Pie Chart", border = 0, align = "Center")
    pdf.image("img/pie_chart_client_portfolio.png", x = 10, y = 75, w = WIDTH-20)
 
 


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
