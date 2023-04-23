# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:07:02 2023

@author: suij2
"""
import pandas as pd
import matplotlib as plt

def create_bollinger_bands(df, window=21, no_of_std=1, column_name=''):
    '''Creates bollinger bands using dataframes from pandas'''
    if not column_name:
        column_name = df.columns[0]
    rolling_mean = df[column_name].rolling(window=window).mean()
    rolling_std = df[column_name].rolling(window=window).std()
    
    upper_bound = rolling_mean + (rolling_std * no_of_std)
    lower_bound = rolling_mean - (rolling_std * no_of_std)
    
    bollinger_bands = pd.DataFrame(index=df.index)
    bollinger_bands['Observation'] = df[column_name]
    bollinger_bands['RollingMean'] = rolling_mean
    bollinger_bands['UpperBound'] = upper_bound
    bollinger_bands['LowerBound'] = lower_bound
    
    return bollinger_bands

def create_long_short_position(df):
    '''creates long/short positions'''
    position_df = pd.DataFrame(index=df.index)
    # makes position column to 0
    position_df['Position'] = 0
    
    # loops through the df and determines the position
    for i in range(1, len(df)):
        #makes long short 1 , -1 respectively
        if df['Observation'][i] > df['UpperBound'][i] and df['Observation'][i - 1] <= df['UpperBound'][i - 1]:
            position_df['Position'][i] = 1
        elif df['Observation'][i] < df['LowerBound'][i] and df['Observation'][i - 1] >= df['LowerBound'][i - 1]:
            position_df['Position'][i] = -1
        else:
            position_df['Position'][i] = position_df['Position'][i - 1]
    
    return position_df

def calculate_long_short_returns(df, position, column_name=''):
    '''calculates long_short_returns'''
    if not column_name:
        column_name = df.columns[0]
    
    daily_returns = df[column_name].pct_change()
    market_return = daily_returns
    strategy_return = daily_returns * position['Position'].shift(1)
    
    abnormal_return = strategy_return - market_return #calcs the difference

    returns_df = pd.DataFrame(index=df.index)
    returns_df['Market Return'] = market_return
    returns_df['Strategy Return'] = strategy_return
    returns_df['Abnormal Return'] = abnormal_return
    
    return returns_df


def plot_cumulative_returns(df):
    '''plots the cum return of the input dataframe'''
    # calculate cumulative returns for each column
    cumulative_returns = (1 + df).cumprod()
    cumulative_returns.plot()
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.title('Cumulative Returns')
    plt.legend(loc='best')
    plt.show()
        