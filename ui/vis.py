import matplotlib.pyplot as plt
import numpy as np

def save_vis_daily_return_distribution_benchmark(daily_returns_df_benchmark):
    first = daily_returns_df_benchmark['QQQ']
    second = daily_returns_df_benchmark["SPY"]
    third = daily_returns_df_benchmark["IEF"]
    fourth = daily_returns_df_benchmark["DIA"]

    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(14)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.set(title = "Daily Return Distribution Benchmarks\n(2019-2022)",
        xlabel = "Daily Return",
        ylabel = "Frequency")

    plt.hist(fourth, bins=10, color='#c491d9', label="DIA")
    plt.hist(second, bins=10, color='#F8A241', label="SPY")
    plt.hist(first, bins=10, color='#f0f06e', label="QQQ")
    plt.hist(third, bins=10, color='#4f92ff', label="IEF")
    plt.savefig("./img/daily_return_benchmark.png")

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

def save_vis_daily_return_distribution_client(daily_returns_df_client):

    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(14)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.set(title = "Daily Return Distribution Client Profile\n(2019-2022)",
        xlabel = "Daily Return",
        ylabel = "Frequency")
        
    plt.hist(daily_returns_df_client, color='#2f852a )

    plt.savefig("./img/daily_return_client.png")

def save_vis_cumulative_return_distribution_client(cumulative_returns_df_client):

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

def plot_mc_sp(mc_sp):
    # Plot simulation outcomes
    MC_sim_line_plot = mc_sp.plot_simulation()
    # # Save the plot for future use
    MC_sim_line_plot.get_figure().savefig("./img/mc_sp.png", bbox_inches="tight")

def plot_mc_client(mc_client):
    # Plot simulation outcomes
    MC_sim_line_plot = mc_client.plot_simulation()
    # # Save the plot for future use
    MC_sim_line_plot.get_figure().savefig("./img/mc_client.png", bbox_inches="tight")

def pie_chart_client_portfolio(client_portfolio, tickers):
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = tickers
    sizes = client_portfolio

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig("./img/pie_chart_client_portfolio.png")




