# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:24:35 2023

@author: suij2

a11task1.py
Assignment 11: Quantifying Investment Risk.

Functions to plot drawdowns in line graphs and histograms
"""

import numpy as np
import scipy.stats as st
import pandas as pd
import matplotlib.pyplot as plt
from a9task1 import MCStockSimulator

def compute_drawdown(prices):
    '''returns a pandas DataFrame with new columns prev_max the drawdown values in dollars and in percentage '''
    #Copy prices data
    prices_df = pd.DataFrame(data=prices, columns=['price'])
    
    #Adding and computing the new columns
    prices_df['prev_max'] = prices_df['price'].cummax()
    prices_df['dd_dollars'] = prices_df['prev_max'] - prices_df['price']
    prices_df['dd_pct'] = prices_df['dd_dollars'] / prices_df['prev_max']
    
    return prices_df

def plot_drawdown(df):
    '''plots the 2 graphs one is price and prev_max the other is drawdown pct'''
    plt.figure(); df[['price','prev_max']].plot(title = "Price and Previous Maximum"); plt.legend(loc='best')
    
    plt.figure(); df[['dd_pct']].plot(title = "Drawdown Percentage"); plt.legend(loc='best')
    

def run_mc_drawdown_trials(init_price, years, r, sigma, trial_size, num_trials):
    '''simulates possible drawdowns using montecarlo simulation and then returns a pandaS series to show possible drawdowns'''
    #Empty matrix to store all drawdown pct
    trial_results = np.zeros(num_trials)
                             
    for i in range(num_trials):
        MCSim = MCStockSimulator(init_price, years, r, sigma, trial_size)
        prices = MCSim.generate_simulated_stock_values()
        mc_dd = compute_drawdown(prices)
        #Getting only the dd_pct
        mc_pct = pd.DataFrame(data=mc_dd['dd_pct'])
        #Getting Max drawdown each trial
        ddHigh = mc_pct.max()
        
        #Adding Max drawdown to trial_results
        trial_results[i] = ddHigh
        
    
    return pd.Series(trial_results)