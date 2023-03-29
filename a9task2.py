# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:35:09 2023

@author: JimmyMan
"""

import numpy as np
from scipy.stats import norm
from MCStockSimulator import MCStockSimulator

class MCStockOption(MCStockSimulator):
    '''base class for all options'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''parent constructor for all options'''
        super().__init__(s, t, r, sigma, nper_per_year, num_trials)
        self.x = x
        self.num_trials = num_trials

    def __repr__(self):
        '''gives string representation of option'''
        return f"MCStockOption (s=${self.s:,.2f}, x=${self.x:,.2f}, t={self.t:.2f} (years), r={self.r:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})"

    def value(self):
        '''calculates value of the chosen type of option'''
        print("Base class MCStockOption has no concrete implementation of .value().")
        return 0

    def stderr(self):
        if self.num_trials == 0:
            return 0
        return self.stdev() / np.sqrt(self.num_trials)
    
class MCEuroCallOption(MCStockOption):
    '''euro call option'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
    
    def value(self):
        '''calculates value of the chosen type of option'''
        

class MCEuroPutOption(MCStockOption):
    '''euro put option'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

class MCAsianCallOption(MCStockOption):
    '''asian call option'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

class MCAsianPutOption(MCStockOption):
    '''asian put option'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

class MCLookbackCallOption(MCStockOption):
    '''lookback call option'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

class MCLookbackPutOption(MCStockOption):
    '''lookback put option'''
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)


    
    