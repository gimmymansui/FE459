# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:40:33 2023

@author: JimmyMan
"""

import numpy as np
import matplotlib.pyplot as plt

class MCStockSimulator:
    def __init__(self, s, t, mu, sigma, nper_per_year):
        self.s = s
        self.t = t
        self.mu = mu
        self.sigma = sigma
        self.nper_per_year = nper_per_year
    
    def __repr__(self):
        return f"MCStockSimulator (s=${self.s:.2f}, t={self.t:.2f} (years), mu={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year})"
    
    def generate_simulated_stock_returns(self):
        n = int(self.nper_per_year * self.t)
        dt = 1 / self.nper_per_year
        drift = (self.mu - 0.5 * self.sigma ** 2) * dt
        diffusion = self.sigma * np.sqrt(dt) * np.random.normal(size=n)
        return drift + diffusion
    
    def generate_simulated_stock_values(self):
        returns = self.generate_simulated_stock_returns()
        prices = np.zeros(len(returns)+1)
        prices[0] = self.s
        for i in range(1, len(prices)):
            prices[i] = prices[i-1] * np.exp(returns[i-1])
        return prices

    def plot_simulated_stock_values(self, num_trials=1):
        for i in range(num_trials):
            simulated_values = self.generate_simulated_stock_values()
            time_axis = np.arange(len(simulated_values)) * (self.t / len(simulated_values))
            plt.plot(time_axis, simulated_values)
        plt.xlabel('years')
        plt.ylabel('$ value')
        plt.title(f'{num_trials} simulated trials')
        plt.show()