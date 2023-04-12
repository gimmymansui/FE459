# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:55:18 2023

@author: JimmyMan
"""

from a10task2 import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

    
def plot_stock_prices(symbols):
    """
    Creates a graph of the historical stock prices for several stocks.

    Parameters:
    symbols (list): A list of stock symbols.

    Returns:
    None.
    """
    dfs = []
    for symbol in symbols:
        df = pd.read_csv(f'{symbol}.csv', index_col=0, parse_dates=True)
        df.rename(columns={'Adj Close': symbol}, inplace=True)
        df_monthly = df.resample('M').last()
        dfs.append(df_monthly)

    prices = pd.concat(dfs, axis=1)
    prices.plot(y = symbols)
    plt.title('Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.show()

def plot_stock_cumulative_change(symbols):
    """
    Creates a graph of the cumulative change in stock prices for several stocks.

    Parameters:
    symbols (list): A list of stock symbols.

    Returns:
    None.
    """
    dfs = []
    for symbol in symbols:
        df = pd.read_csv(f'{symbol}.csv', index_col=0, parse_dates=True)
        df_monthly = df.resample('M').last()
        df_monthly['monthly_return'] = df_monthly['Adj Close'].pct_change()
        df_monthly['cumulative_return'] = (1 + df_monthly['monthly_return']).cumprod() - 1
        dfs.append(df_monthly[['cumulative_return']])

    prices = pd.concat(dfs, axis=1)
    ax = prices.plot()
    ax.legend(symbols, loc='best')  # pass symbols to legend() method
    plt.title('Cumulative Change in Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.show()
    
def plot_efficient_frontier(symbols):
    """
    Plots an efficient frontier of portfolios with the stocks listed in the symbols array

    Parameters:
    symbols (list): A list of stock symbols.

    Returns:
    None.
    """
    # get returns and covariance matrix
    returns = get_stock_returns_from_csv_files(symbols)
    covar = np.matrix(get_covariance_matrix(returns))

    # calculate average return and create matrix of returns
    avg_returns = returns.mean()
    R = np.matrix(avg_returns).T

    # create set of desired rates of return
    glo_min_var_portfolio = calc_global_min_variance_portfolio(covar)
    target_rs = np.linspace(glo_min_var_portfolio[0, 0], 0.08, num=100000)
    target_rs = np.array(target_rs)
    low = np.linspace(-0.08, glo_min_var_portfolio[0, 0], num=100000)
    low = np.array(low)
    target_rs = np.concatenate((target_rs, low), axis = None)
    
    # calculate standard deviations of efficient portfolios
    eff_stdevs = calc_efficient_portfolios_stdev(R.T, covar, target_rs)
    eff_stdevs = np.array(eff_stdevs)


    # plot efficient frontier
    plt.plot(eff_stdevs, target_rs, '-')
    plt.xlim(0,0.1)
    plt.ylim(-0.08, 0.08)
    plt.title('Efficient Frontier')
    plt.xlabel('Standard Deviation')
    plt.ylabel('Expected Return')

    plt.show()