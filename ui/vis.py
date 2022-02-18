from locale import normalize
import matplotlib.pyplot as plt
import numpy as np

# create a cumulative return distribution benchmark line chart:
def save_vis_cumulative_return_distribution_benchmark(cumulative_returns_df_benchmark):
    # assign variables
    first = cumulative_returns_df_benchmark['QQQ']
    second = cumulative_returns_df_benchmark["SPY"]
    third = cumulative_returns_df_benchmark["IEF"]
    fourth = cumulative_returns_df_benchmark["DIA"]
    fig, ax = plt.subplots()
    # set figure size
    fig.set_figheight(10)
    fig.set_figwidth(14)
    # delete top and right side of the graph's spine
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # assign title and label names
    ax.set(title = "Cumulative Returns Benchmarks\n(2019-2022)",
        xlabel = "Year",
        ylabel = "Return\n(%)") # \n is used to seperate lines of text in a title/label
    # plot the benchmark ETFs and set their label name/color
    plt.plot(first, label = "QQQ", color='#f0f06e')
    plt.plot(second, label = "SPY", color='#F8A241')
    plt.plot(third, label = "IEF", color='#4f92ff')
    plt.plot(fourth, label = "DIA", color='#c491d9')
    # rotate x-axis ticks by 45-degrees
    plt.xticks(rotation = 45)
    plt.legend()
    # save the visualization as a png file
    plt.savefig("./img/cumulative_return_benchmark.png")

# create a 45-day rolling volatility visualization comparing benchmark ETFs and the client portfolio:
def save_45_day_rolling_volitility_benchmark(daily_returns_df_benchmark, daily_returns_df_client):
    # calculate the 45-day rolling volatility for benchmark/client portfolio.
    daily_45_rolling_returns_benchmark = daily_returns_df_benchmark.rolling(45).std()*np.sqrt(45)
    daily_45_rolling_returns_client = daily_returns_df_client.rolling(45).std()*np.sqrt(45)
    daily_45_rolling_returns_client = daily_45_rolling_returns_client.mean(axis=1)
    # assign variables
    first_45 = daily_45_rolling_returns_benchmark['QQQ']
    second_45 = daily_45_rolling_returns_benchmark["SPY"]
    third_45 = daily_45_rolling_returns_benchmark["IEF"]
    fourth_45 = daily_45_rolling_returns_benchmark["DIA"]
    fifth_45 = daily_45_rolling_returns_client
    fig, ax = plt.subplots()
    # set figure size
    fig.set_figheight(10)
    fig.set_figwidth(14)
    # delete top and right side of the graph's spine
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # assign title and label names    
    ax.set(title = "Rolling 45-day Volatility Benchmarks with Client Portfolio Components\n(2019-2022)",
        xlabel = "Time",
        ylabel = "Volatility")
    # plot the benchmark ETFs/client portfolio and set their label name/color
    plt.plot(fifth_45, label = "Client Portfolio", color='#2f852a')
    plt.plot(first_45, label = "QQQ", color='#f0f06e')
    plt.plot(second_45, label = "SPY", color='#F8A241')
    plt.plot(third_45, label = "IEF", color='#4f92ff')
    plt.plot(fourth_45, label = "DIA", color='#c491d9')
    # rotate x-axis ticks by 45-degrees
    plt.xticks(rotation = 45)
    plt.legend()
    # save the visualization as a png file   
    plt.savefig("./img/45_day_vol_benchmark.png")

# create a client portfolio cumulative return line chart:
def save_vis_cumulative_return_distribution_client(cumulative_returns_df_client):
    fig, ax = plt.subplots()
    # set figure size
    fig.set_figheight(10)
    fig.set_figwidth(14)
    # delete top and right side of the graph's spine
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # assign title and label names
    ax.set(title = "Cumulative Returns Client Profile\n(2019-2022)",
        xlabel = "Year",
        ylabel = "Increase\n(%)")
    # plot the client portfolio cumulative returns and set the color
    plt.plot(cumulative_returns_df_client, color='#2f852a')
    # rotate x-axis ticks by 45-degrees
    plt.xticks(rotation = 45)
    # save the visualization as a png file    
    plt.savefig("./img/cumulative_return_client.png")

# create a client portfolio 45-day rolling volatility:
def save_45_day_rolling_volitility_client(daily_returns_df_client):
    # calculate the 45-day rolling volatility of each ETF found in the client portoflio
    daily_45_rolling_returns = daily_returns_df_client.rolling(45).std()*np.sqrt(45)
    daily_45_rolling_returns_client=daily_45_rolling_returns.mean(axis=1)
    fig, ax = plt.subplots()
    # set figure size    
    fig.set_figheight(10)
    fig.set_figwidth(14)
    # delete top and right side of the graph's spine  
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # assign a title and x/y label names for the visualization   
    ax.set(title = "Rolling 45-day Volatility Client Profile\n(2019-2022)",
        xlabel = "Time",
        ylabel = "Volatility")
    # plot the client portfolio 45-day rolling volatility and set the color
    plt.plot(daily_45_rolling_returns, color='#b6d7a8')
    plt.plot(daily_45_rolling_returns_client, color='#2f852a')
    # rotate x-axis ticks by 45-degrees
    plt.xticks(rotation = 45)
    # save the visualization as a png file       
    plt.savefig("./img/45_day_vol_client.png")

# create a cumulative return visualization that compares the client portoflio to the SPY ETF:
def save_vis_cumulative_return_benchmark_client(cumulative_returns_df_benchmark, cumulative_returns_df_client):
    # assign variables
    first = cumulative_returns_df_benchmark['SPY']
    second = cumulative_returns_df_client
    fig, ax = plt.subplots()
    # set figure size 
    fig.set_figheight(10)
    fig.set_figwidth(14)
    # delete top and right side of the graph's spine     
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # assign a title and x/y label names for the visualization      
    ax.set(title = "Cumulative Returns S&P v. Client Profile\n(2019-2022)",
        xlabel = "Year",
        ylabel = "Increase\n(%)")
    # plot the cumulative return for client portfolio/SPY and set the color
    plt.plot(first, label = "SPY", color='#F8A241')
    plt.plot(second, label = "Client Profile", color='#2f852a')
    # rotate x-axis ticks by 45-degrees    
    plt.xticks(rotation = 45)
    plt.legend()
    # save the visualization as a png file 
    plt.savefig("./img/cumulative_return_benchmark_client.png")

# create a monte carlo visualization using SPY data:
def plot_mc_sp(mc_sp):
    # Plot simulation outcomes
    MC_sim_line_plot = mc_sp.plot_simulation()
    # # Save the plot for future use
    MC_sim_line_plot.get_figure().savefig("./img/mc_sp.png", bbox_inches="tight")
             

# create a monte carlo visualization using client portfolio data:
def plot_mc_client(mc_client):
    # plot simulation outcomes
    MC_sim_line_plot = mc_client.plot_simulation()
    # save the plot for future use
    MC_sim_line_plot.get_figure().savefig("./img/mc_client.png", bbox_inches="tight")
            

# create a pie chart which consists of the client portfolio ETF compositon:
def pie_chart_client_portfolio(client_portfolio, tickers):
    # pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = tickers
    sizes = client_portfolio
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, normalize=True)
    ax1.axis('equal') # equal aspect ratio ensures that pie is drawn as a circle
    # save the visualization as a png file
    plt.savefig("./img/pie_chart_client_portfolio.png")
            





