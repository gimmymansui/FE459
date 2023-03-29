# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:41:12 2023

@author: suij2
"""
from a8task1 import *
def generate_option_value_table(s, x, t, sigma, rf, div):
    """generates a table of option price changes given changes in the underlying stock

    Args:
        s (float): the current price of the underlying asset
        x (float): the current strike price of the option
        t (float): the option maturity time in years
        sigma (float): the annualized standard deviation of returns
        rf (float): the annualized risk free rate of return
        div (float): the annualized dividend rate; assume continuous dividends rate
    """
    price = s - 10
    call = BSMEuroCallOption(price, x, t, sigma, rf, div)
    put = BSMEuroPutOption(price, x, t, sigma, rf, div)
    n = 21
    
    print("Change in option values w.r.t. change in stock prices:")
    print("price".center(12," ") + "call value".center(16, " ") + "put value".center(14, " ") + "call delta".center(14, " ") + "put delta".center(13, " "))
    for i in range(n):
        print(f"$   {call.getS():<8.2f}{call.value():>12.4f}{put.value():>14.4f}{call.delta():>14.4f}{put.delta():>14.4f}")
        price += 1
        call.setprice(price)
        put.setprice(price)

def calculate_implied_volatility(option, lastprice):
    """calculates the implied volatility of an option given its last price

    Args:
        option (BSMOption): BSMOption object
        lastprice (float): last market price of the option

    Returns:
        float: implied volatility as a decimal
    """
    tolerance = 0.00001
    max_iterations = 1000
    sigma = 0.5
    iteration = 0
    
    while True:
        price = option.value()
        diff = price - lastprice
        if abs(diff) < tolerance or iteration >= max_iterations:
            break
        v = option.vega()
        sigma = sigma - diff / v
        option.setsigma(sigma)
        iteration += 1
    
    return sigma
        
    