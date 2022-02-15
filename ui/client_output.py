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


def create_pdf(full_name):
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
    pdf.write(5, f"Thank you for trusting our team with your information.  We believe that this report will be beneficial and assist you on your financial journey.  In the pages that follow, you will find educational material custom tailored to your risk tolerance, investment horizon, and preferred investment strategy.  Our investment advisor will follow up with you in a couple of days to answer any questions that you have and assist you in implementing your investment plan.  Welcome to the JACK Investment family.")
    pdf.set_font('Arial', '', 12)
    pdf.ln(22)
    pdf.multi_cell(WIDTH/2-10,5, "In the pages that follow, you will find your Risk Assessment Score, your Investment Horizon Score, and your Investment Strategy.  This report has been created using cutting edge analysis to provide you with the best investment alternatives based upon your criteria.  If any of the information in the chart to the right is incorrect, please notify your account representative as this report is created using this financial and investment data.", border = 0)
    pdf.image("./img/clientdata.png", x = 110, y = 120, w = WIDTH/2-10)
    pdf.ln(18)
    pdf.set_left_margin(WIDTH/2+5)
    pdf.multi_cell(WIDTH/2-10,5, "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi.", border = 0)
    #pdf.image("img/mc.png", x = 10, y = 190, w = WIDTH/2-10)
    pdf.set_left_margin(10)
    # page 2
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.image("./img/letterhead2.png", 0, 0, WIDTH)
    pdf.ln(22)
    pdf.set_left_margin(10)
    pdf.multi_cell(WIDTH/2-10,5, "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet.", border = 0)
    #pdf.image("img/chart.png", x = 110, y = 130, w = WIDTH/2-10)
    #pdf.set_left_margin(WIDTH/2+5)
    pdf.multi_cell(WIDTH/2-10,5, "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi.", border = 0)
    #pdf.image("img/chart.png", x = 10, y = 190, w = WIDTH/2-10)
    #pdf.ln(10)
    #pdf.write(4, f"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,")
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
