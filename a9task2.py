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
    '''base class for all options'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''base constructor for all options'''
        super().__init__(s, t, r, sigma, nper_per_year)
        self.x = x
        self.num_trials = num_trials

    
    def __repr__(self):
        '''gives string representation of option'''
        return f"{self.__class__.__name__} (s=${self.s:,.2f}, x=${self.x:,.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})"

    def value(self):
        '''calculates value of the chosen type of option'''
        print("Base class MCStockOption has no concrete implementation of .value().")
        return 0

    def stderr(self):
        '''polymorphic template for stderr'''
        if 'stdev' in dir(self):
            return self.stdev / np.sqrt(self.num_trials)
        return 0
    
class MCEuroCallOption(MCStockOption):
    '''euro call option'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
    
    def value(self):
        '''value of euro puts'''
        trials = []
        for i in range(self.num_trials): #loops through all the trials runs the calculation and takes the mean of those calculations and returns it this is the process for all option types.
            prices = self.generate_simulated_stock_values()
            payoff = max(prices[-1] - self.x, 0)
            trials.append(payoff * np.exp(-self.mu * self.t))
        self.mean = np.mean(trials)
        self.stdev = np.std(trials)
        return self.mean
        

class MCEuroPutOption(MCStockOption):
    '''euro put option'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''initialises object'''
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
        
    def value(self):
        '''calculates value of euro put option'''
        trials = []
        for i in range(self.num_trials):
            prices = self.generate_simulated_stock_values()
            payoff = max(-prices[-1] + self.x, 0)
            trials.append(payoff * np.exp(-self.mu * self.t))
        self.mean = np.mean(trials)
        self.stdev = np.std(trials)
        return self.mean
        
class MCAsianCallOption(MCStockOption):
    '''Asian call option class'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''constructor for Asian call option'''
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def value(self):
        '''calculate value of Asian call option'''
        trials = []
        for i in range(self.num_trials):
            prices = self.generate_simulated_stock_values()
            avg_price = np.mean(prices)
            payoff = max(avg_price - self.x, 0)
            trials.append(payoff * np.exp(-self.mu * self.t))
        self.mean = np.mean(trials)
        self.stdev = np.std(trials)
        return self.mean

        
class MCAsianPutOption(MCStockOption):
    '''Asian put option class'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''constructor for Asian put option'''
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def value(self):
        '''calculate value of Asian put option'''
        trials = []
        for i in range(self.num_trials):
            prices = self.generate_simulated_stock_values()
            avg_price = np.mean(prices)
            payoff = max(self.x - avg_price, 0)
            trials.append(payoff * np.exp(-self.mu * self.t))
        self.mean = np.mean(trials)
        self.stdev = np.std(trials)
        return self.mean
    
class MCLookbackCallOption(MCStockOption):
    '''Lookback call option class'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''constructor for Lookback call option'''
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def value(self):
        '''calculate value of Lookback call option'''
        trials = []
        for i in range(self.num_trials):
            prices = self.generate_simulated_stock_values()
            max_price = np.max(prices)
            payoff = np.maximum(max_price - self.x, 0)
            trials.append(payoff * np.exp(-self.mu * self.t))
        self.mean = np.mean(trials)
        self.stdev = np.std(trials)
        return self.mean

class MCLookbackPutOption(MCStockOption):
    '''Lookback put option class'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''constructor for Lookback put option'''
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def value(self):
        '''calculate value of Lookback put option'''
        trials = []
        for i in range(self.num_trials):
            prices = self.generate_simulated_stock_values()
            min_price = np.min(prices)
            payoff = max(-min_price + self.x, 0)
            trials.append(payoff * np.exp(-self.mu * self.t))
        self.mean = np.mean(trials)
        self.stdev = np.std(trials)
        return self.mean



    
    