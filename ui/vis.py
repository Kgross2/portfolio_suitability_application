import matplotlib.pyplot as plt
import numpy as np

# def save_vis_daily_return_distribution_benchmark(daily_returns_df_benchmark):
#     first = daily_returns_df_benchmark['QQQ']
#     second = daily_returns_df_benchmark["SPY"]
#     third = daily_returns_df_benchmark["IEF"]
#     fourth = daily_returns_df_benchmark["DIA"]

#     fig, ax = plt.subplots()
#     fig.set_figheight(10)
#     fig.set_figwidth(14)
#     ax.spines['top'].set_color('none')
#     ax.spines['right'].set_color('none')
#     ax.set(title = "Daily Return Distribution Benchmarks\n(2019-2022)",
#         xlabel = "Daily Return",
#         ylabel = "Frequency")

#     plt.hist(fourth, bins=10, color='#c491d9', label="DIA")
#     plt.hist(second, bins=10, color='#F8A241', label="SPY")
#     plt.hist(first, bins=10, color='#f0f06e', label="QQQ")
#     plt.hist(third, bins=10, color='#4f92ff', label="IEF")
#    plt.savefig("./img/daily_return_benchmark.png")
     # Scrapped

def save_vis_cumulative_return_distribution_benchmark(cumulative_returns_df_benchmark):
    first = cumulative_returns_df_benchmark['QQQ']
    second = cumulative_returns_df_benchmark["SPY"]
    third = cumulative_returns_df_benchmark["IEF"]
    fourth = cumulative_returns_df_benchmark["DIA"]

    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(14)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.set(title = "Cumulative Returns Benchmarks\n(2019-2022)",
        xlabel = "Year",
        ylabel = "Increase\n(%)")

    plt.plot(first, label = "QQQ", color='#f0f06e')
    plt.plot(second, label = "SPY", color='#F8A241')
    plt.plot(third, label = "IEF", color='#4f92ff')
    plt.plot(fourth, label = "DIA", color='#c491d9')
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
    plt.legend()
    plt.savefig("./img/cumulative_return_benchmark.png")
        # This figure displays the cumulative return of the benchmark ETFs.
        # Cumulative return measures the total change in an investment's value over a specific 
        # period. The y-axis label represents the percentage increase in value. (.75=75% increase)
        # We can see that during a dip around 2020-03 where all the ETFs fell, besides IEF, QQQ
        # experienced a larger boost in value compared to the other ETFs. This allowed QQQ to
        # reach a return of 1.18 while the second highest return, SPY, was 0.69. IEF has the
        # lowest cumulative return of the benchmark but it displayed excellent resiliance during the
        # 2020-03 market dip.
        
            # BENCHMARK
        

def save_45_day_rolling_volitility_benchmark(daily_returns_df_benchmark):
    daily_45_rolling_returns = daily_returns_df_benchmark.rolling(45).std()*np.sqrt(45)

    first_45 = daily_45_rolling_returns['QQQ']
    second_45 = daily_45_rolling_returns["SPY"]
    third_45 = daily_45_rolling_returns["IEF"]
    fourth_45 = daily_45_rolling_returns["DIA"]

    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(14)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.set(title = "Rolling 45-day Volatility Benchmarks\n(2019-2022)",
        xlabel = "Time",
        ylabel = "Volatility")

    plt.plot(first_45, label = "QQQ", color='#f0f06e')
    plt.plot(second_45, label = "SPY", color='#F8A241')
    plt.plot(third_45, label = "IEF", color='#4f92ff')
    plt.plot(fourth_45, label = "DIA", color='#c491d9')
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
    plt.legend()
    plt.savefig("./img/45_day_vol_benchmark.png")
        # This visualization measures the 45-day rolling volatility of our benchmark ETFs.
        # Volatility determines the risk associated with an investment, as the volatility rises the
        # potential gain or loss increases.
        # This graph is set over a time period of three years, (2019-20-12 - 2022-02-12).
        # We can see that QQQ on average has the highest volatility among the ETFs, which means it
        # poses the most risk. We can also see that SPY and DIA share a similar
        # volatility level overall, both investments pose a similar risk. Finally, we look at
        # IEF, this ETF has the lowest volatility of the benchmark by far, therefore it is the safest
        # investment.
        
            # BENCHMARK

# def save_vis_daily_return_distribution_client(daily_returns_df_client):

#     fig, ax = plt.subplots()
#     fig.set_figheight(10)
#     fig.set_figwidth(14)
#     ax.spines['top'].set_color('none')
#     ax.spines['right'].set_color('none')
#     ax.set(title = "Daily Return Distribution Client Profile\n(2019-2022)",
#         xlabel = "Daily Return",
#         ylabel = "Frequency")
        
#     plt.hist(daily_returns_df_client, color='#2f852a )

#     plt.savefig("./img/daily_return_client.png")
        # This graph uses daily return distribution to compare each component of the program 
        # selected ETF. We can see the entire portfolio broken down into specific assets and compare
        # their daily return distribution.
        
        # scrapped


def save_vis_cumulative_return_distribution_client(cumulative_returns_df_client):
        # Should be renamed without distribution, i think?

    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(14)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.set(title = "Cumulative Returns Client Profile\n(2019-2022)",
        xlabel = "Year",
        ylabel = "Increase\n(%)")

    plt.plot(cumulative_returns_df_client, color='#2f852a')
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
    plt.savefig("./img/cumulative_return_client.png")

        # This visualization displays the cumulative returns of the selected client portfolio
        # This portfolio shares the same dip as the benchmark ETFs, this is because the value of the
        # entire market dropped around 2020-03. The y-axis represents change in the total value
        # of the ETF.
             
        # NEEDS WORK
        
            # CLIENT

def save_45_day_rolling_volitility_client(daily_returns_df_client):
    daily_45_rolling_returns = daily_returns_df_client.rolling(45).std()*np.sqrt(45)

    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(14)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.set(title = "Rolling 45-day Volatility Client Profile\n(2019-2022)",
        xlabel = "Time",
        ylabel = "Volatility")

    plt.plot(daily_45_rolling_returns, color='#2f852a')
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
    plt.savefig("./img/45_day_vol_client.png")
        # This visualization uses 45-day rolling volatility to compare each ETF found in the selected
        # client portfolio. Each line represents a different ETF that makes up the
        # portfolio. We can see that there is a mix of volatility in the portfolio, this allows a
        # portfolio to have more balance.

def save_vis_cumulative_return_benchmark_client(cumulative_returns_df_benchmark, cumulative_returns_df_client):
    first = cumulative_returns_df_benchmark['SPY']
    second = cumulative_returns_df_client

    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(14)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.set(title = "Cumulative Returns S&P v. Client Profile\n(2019-2022)",
        xlabel = "Year",
        ylabel = "Increase\n(%)")

    plt.plot(first, label = "SPY", color='#F8A241')
    plt.plot(second, label = "Client Profile", color='#2f852a)
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
    plt.legend()
    plt.savefig("./img/cumulative_return_benchmark_client.png")
             
    # This visualization compares the cumulative return of the selected client portfolio
    # to the SPY ETF. This graph shows us that the portfolio follows a similar pattern to SPY but
    # the values change at a lower rate. This is because SPY's price is based on the S&P 500 which
    # reflects the overarching market and the market experienced a large increase in value after the 
    # 2020-03 dip.


def plot_mc_sp(mc_sp):
    # Plot simulation outcomes
    MC_sim_line_plot = mc_sp.plot_simulation()
    # # Save the plot for future use
    MC_sim_line_plot.get_figure().savefig("./img/mc_sp.png", bbox_inches="tight")
             
        #Need to work on

def plot_mc_client(mc_client):
    # Plot simulation outcomes
    MC_sim_line_plot = mc_client.plot_simulation()
    # # Save the plot for future use
    MC_sim_line_plot.get_figure().savefig("./img/mc_client.png", bbox_inches="tight")
             
        #Need to work on

def pie_chart_client_portfolio(client_portfolio, tickers):
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = tickers
    sizes = client_portfolio

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig("./img/pie_chart_client_portfolio.png")
             # This visualization shows us each ETF that makes up the selected client portfolio.
             # A pie chart is used because it is a simple graph for users to understand exactly how
             # the recommend portfolio is composed. It also provides users a faster understanding
             # of the portfolio composition compared to other visualization options.
             
             # its on the front page of pdf, must be easily readable





