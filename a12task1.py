# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:07:02 2023

@author: suij2
"""
import pandas as pd
import matplotlib as plt

def create_bollinger_bands(df, window=21, no_of_std=1, column_name=''):
    if not column_name:
        column_name = df.columns[0]
    # Calculate the rolling mean and standard deviation
    rolling_mean = df[column_name].rolling(window=window).mean()
    rolling_std = df[column_name].rolling(window=window).std()
    
    # Calculate the upper and lower Bollinger Bands
    upper_bound = rolling_mean + (rolling_std * no_of_std)
    lower_bound = rolling_mean - (rolling_std * no_of_std)
    
    # Create a new DataFrame to store the results
    bollinger_bands = pd.DataFrame(index=df.index)
    bollinger_bands['Observation'] = df[column_name]
    bollinger_bands['RollingMean'] = rolling_mean
    bollinger_bands['UpperBound'] = upper_bound
    bollinger_bands['LowerBound'] = lower_bound
    
    return bollinger_bands

def create_long_short_position(df):
    position_df = pd.DataFrame(index=df.index)
    # Initialize the Position column to 0
    position_df['Position'] = 0
    
    # Loop through the DataFrame and determine the position
    for i in range(1, len(df)):
        # Create a long position when the Observation crosses above the UpperBound
        if df['Observation'][i] > df['UpperBound'][i] and df['Observation'][i - 1] <= df['UpperBound'][i - 1]:
            position_df['Position'][i] = 1
        # Create a short position when the Observation crosses below the LowerBound
        elif df['Observation'][i] < df['LowerBound'][i] and df['Observation'][i - 1] >= df['LowerBound'][i - 1]:
            position_df['Position'][i] = -1
        # Hold the previous position
        else:
            position_df['Position'][i] = position_df['Position'][i - 1]
    
    return position_df

def calculate_long_short_returns(df, position, column_name=''):
    if not column_name:
        column_name = df.columns[0]
    
        # Calculate the daily returns
    daily_returns = df[column_name].pct_change()
    
    # Calculate the market returns
    market_return = daily_returns
    
    # Calculate the strategy returns
    strategy_return = daily_returns * position['Position'].shift(1)
    
    # Calculate the abnormal returns
    abnormal_return = strategy_return - market_return
    
    # Create a new DataFrame to store the results
    returns_df = pd.DataFrame(index=df.index)
    returns_df['Market Return'] = market_return
    returns_df['Strategy Return'] = strategy_return
    returns_df['Abnormal Return'] = abnormal_return
    
    return returns_df


def plot_cumulative_returns(df):
    # Calculate cumulative returns for each column
    cumulative_returns = (1 + df).cumprod()
    cumulative_returns.plot()
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.title('Cumulative Returns')
    plt.legend(loc='best')
    plt.show()
        