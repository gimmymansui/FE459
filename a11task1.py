# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:23:22 2023

@author: suij2

a11task1.py
Assignment 11: Quantifying Investment Risk.

Functions to calculate historical and current value at risk
"""

import numpy as np
import scipy.stats as st
import pandas as pd

def compute_model_var_pct(mu, sigma, x, n):
    '''computes value at risk as a floating point decimal'''
    Z = st.norm.ppf(1-x)
    #Calculates the valRisk using the formula given.
    valRisk = mu*n + Z*sigma*np.sqrt(n)
    return valRisk

def compute_historical_var_pct(returns, x, n):
    ''' returns historical value at risk as a floating point decimal'''
    sortedReturns = returns.sort_values()
    
    # Calculates the index determined by the confidence level x sort of like a percentage 'index'
    nIndex = int((1 - x / 100) *len(returns))
    worstReturns = sortedReturns.iloc[nIndex]
    historicalVar = worstReturns*np.sqrt(n)
    
    return historicalVar