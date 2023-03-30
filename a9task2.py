# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:35:09 2023

@author: JimmyMan
"""

import numpy as np
from scipy.stats import norm
from a9task1 import MCStockSimulator
import math

class MCStockOption(MCStockSimulator):
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, t, r, sigma, nper_per_year)
        self.x = x
        self.r = r
        self.num_trials = num_trials
        self.values = self.generate_simulated_stock_values()
        self.stdev = np.std(self.values)
        self.mean = np.mean(self.values)

    
    def __repr__(self):
        '''gives string representation of option'''
        return f"MCStockOption (s=${self.s:,.2f}, x=${self.x:,.2f}, t={self.t:.2f} (years), mu={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})"

    def value(self):
        '''calculates value of the chosen type of option'''
        print("Base class MCStockOption has no concrete implementation of .value().")
        return 0

    def stderr(self):
        if 'stdev' in dir(self):
            return self.stdev / np.sqrt(self.num_trials)
        return 0
    
class MCEuroCallOption(MCStockOption):
    '''euro call option'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
    
    def value(self):
        '''calculates value of European Call Option'''
        option_price = np.exp(-self.r * self.t) * np.maximum(self.values[-1] - self.x, 0)
        return option_price
        

class MCEuroPutOption(MCStockOption):
    '''euro put option'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
        
    def value(self):
        '''calculates value of the chosen type of option'''
        return max(self.x - self.values[-1], 0)*math.exp(-self.r*self.t)
        
class MCAsianCallOption(MCStockOption):
    '''Asian call option class'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''constructor for Asian call option'''
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def value(self):
        '''calculate value of Asian call option'''
        return np.maximum(self.mean - self.x, 0)*np.exp(self.r*-self.t)

        
class MCAsianPutOption(MCStockOption):
    '''Asian put option class'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''constructor for Asian put option'''
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def value(self):
        '''calculate value of Asian put option'''
        return np.maximum(-self.mean + self.x, 0)*np.exp(self.r*-self.t)
    
class MCLookbackCallOption(MCStockOption):
    '''Lookback call option class'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''constructor for Lookback call option'''
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def value(self):
        '''calculate value of Lookback call option'''
        option_values = []
        for i in range(self.num_trials):
            stock_values = self.generate_simulated_stock_values()
            max_price = np.max(stock_values)
            payoff = max(max_price - self.x, 0)
            option_value = payoff * np.exp(-self.r * self.t)
            option_values.append(option_value)
        return option_values


class MCLookbackPutOption(MCStockOption):
    '''Lookback put option class'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''constructor for Lookback put option'''
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def value(self):
        '''calculate value of Lookback put option'''
        option_values = []
        for i in range(self.num_trials):
            stock_values = self.generate_simulated_stock_values()
            min_price = np.min(stock_values)
            payoff = max(self.x - min_price, 0)
            option_value = payoff * np.exp(-self.r * self.t)
            option_values.append(option_value)
        return option_values



    
    